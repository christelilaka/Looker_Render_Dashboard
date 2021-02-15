from .Interface import Interface

class CreateRenderTask(Interface):
    @classmethod
    def make_call(cls, dash_id, filters):
        dash_body = cls.models.CreateDashboardRenderTask(dashboard_filters=filters)
        result = cls.sdk.create_dashboard_render_task(dashboard_id=1, result_format='pdf', body=dash_body, width=800, height=600)
        return result.id