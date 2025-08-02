import random
from django.shortcuts import render
import plotly.express as px
from sport.models import Workout
from sport.forms import DateForm
from calendar import monthrange


def chart(request):
    year = request.GET.get('year')
    month = request.GET.get('month')
    activity = request.GET.get('activity')
    
    if year:
        workout_running = Workout.objects.filter(workoutActivityType=activity.title(), creationDate__year=int(year), creationDate__month=int(month))
    else:
        last_workout = Workout.objects.order_by('-creationDate')[0].creationDate
        activity = random.choices(['Running', 'Walking'])[0] if activity is None else activity
        workout_running = Workout.objects.filter(workoutActivityType=activity.title(), creationDate__year=last_workout.year, creationDate__month=last_workout.month)
    
    month_duration = {workout.creationDate.day:workout.duration for workout in workout_running}
    if year:
        x = [day for day in range(1, monthrange(int(year), int(month))[1] + 1)]
    else: 
        x = [day for day in range(1, monthrange(last_workout.year, last_workout.month)[1] + 1)]
    y = list()
    for day in x:
        y.append(month_duration.get(day, 0))

    fig = px.bar(
        x=x,
        y=y
    )

    fig.update_layout(title_text=f"Activitiy {activity.title()} Duration",
                      yaxis_title="Duration (min)",
                      xaxis=dict(
                          title="Day",
                          tickmode='linear',
                          dtick=1
                        )

                      )
    chart = fig.to_html()
    context = {'chart': chart, 'form': DateForm(data={'year': year, 
                                                      'month': month,
                                                      'activity': activity})}
    return render(request, 'core/chart.html', context)
