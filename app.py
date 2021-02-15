from helpers import CreateRenderTask, GetStatus, WritePDF
import time

dashboard_id = 1
users = ['George Hill', 'Marvin Miller', 'Sallie Jones', 'Carla Smith']

for user in users:
    filter = 'User+Name=' + user.replace(' ', '+')
    user_name = user.replace(' ', '_')
    render_task_id = CreateRenderTask.make_call(dash_id=dashboard_id, filters=filter)
    
    while not GetStatus.make_call(render_task_id):
        time.sleep(10)
    
    WritePDF.make_call(task_id=render_task_id, user_name=user_name)
    print(f'Render done for {user}')
