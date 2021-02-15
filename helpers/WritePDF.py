from .Interface import Interface

class WritePDF(Interface):
    @classmethod
    def make_call(cls, task_id, user_name):
        out_file = f'./pdf_result/{user_name}.pdf'
        pdf = cls.sdk.render_task_results(render_task_id=task_id)
        with open(out_file, 'wb') as pdf_file:
            pdf_file.write(pdf)