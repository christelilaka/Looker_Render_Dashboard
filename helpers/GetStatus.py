from .Interface import Interface

class GetStatus(Interface):
    @classmethod
    def make_call(cls, id:str):
        result = cls.sdk.render_task(render_task_id=id)
        return result.status == 'success'
