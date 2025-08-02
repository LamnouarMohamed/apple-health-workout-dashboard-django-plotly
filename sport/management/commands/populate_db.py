from django.core.management.base import BaseCommand

from sport.models import FileReference, MetadataEntry, Workout, WorkoutEvent, WorkoutRoute, WorkoutStatistics
from datetime import datetime


class Command(BaseCommand):
    help = 'Creates application data'
    
    def read_xml(self, file_name):
        import xml.etree.ElementTree as ET

        # create element tree object
        tree = ET.parse(file_name) 
        # for every health record, extract the attributes
        root = tree.getroot()
        # record_workout = [x.attrib for x in root.iter('Workout')]

        return root
    
    def handle(self, *args, **kwargs):
        # get or create superuser

        root = self.read_xml(f'sport/data/export.xml')
        for workout in root.iter('Workout'):
            workout_object = Workout.objects.create(workoutActivityType=workout.attrib['workoutActivityType'],
                                                    duration=workout.attrib['duration'],
                                                    durationUnit=workout.attrib['durationUnit'],
                                                    sourceName=workout.attrib['sourceName'],
                                                    # sourceVersion=workout.attrib['sourceVersion'],
                                                    device=workout.attrib['device'],
                                                    creationDate=datetime.strptime(workout.attrib['creationDate'], "%Y-%m-%d %H:%M:%S %z"),
                                                    # startDate=workout.attrib['startDate'],
                                                    # endDate=workout.attrib['endDate']
                                                    )
            for meta_data_entry in workout.findall('MetadataEntry'):
                meta_data_entry_object = MetadataEntry.objects.create(
                    key=meta_data_entry.attrib['key'],
                    value=meta_data_entry.attrib['value'],
                    workout=workout_object
                )
            for workout_event in workout.findall('WorkoutEvent'):
                workout_event_object = WorkoutEvent.objects.create(
                    type=workout_event.attrib['type'],
                    date=workout_event.attrib['date'],
                    duration=workout_event.attrib.get('duration', None),
                    durationUnit=workout_event.attrib.get('durationUnit', None),
                    workout=workout_object
                )
            for workout_statistics in workout.findall('WorkoutStatistics'):
                workout_statistics_object = WorkoutStatistics.objects.create(
                        type=workout_statistics.attrib.get("type"),
                        startDate=workout_statistics.attrib.get("startDate"),
                        endDate=workout_statistics.attrib.get("endDate"),
                        unit=workout_statistics.attrib.get("unit"),
                        sum=workout_statistics.attrib.get("sum"),
                        average=workout_statistics.attrib.get("average"),
                        minimum=workout_statistics.attrib.get("minimum"),
                        maximum=workout_statistics.attrib.get("maximum"),
                        workout=workout_object,
                )
            for workout_route in workout.findall('WorkoutRoute'):
                for file_reference in workout_route.findall('FileReference'):
                    file_reference_object = FileReference.objects.create(
                        path=file_reference.attrib['path']
                    )
                workout_route_object = WorkoutRoute.objects.create(
                    sourceName=workout.attrib['sourceName'],
                    sourceVersion=workout.attrib['sourceVersion'],
                    creationDate=workout.attrib['creationDate'],
                    startDate=workout.attrib['startDate'],
                    endDate=workout.attrib['endDate'],
                    workout=workout_object,
                    file_reference=file_reference_object,
                )
