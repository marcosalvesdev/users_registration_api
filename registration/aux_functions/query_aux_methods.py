class Filter:
    def __init__(self, request, serializer_class, model):
        self.request = request
        self.serializer_class = serializer_class
        self.model = model

    def filter(self) -> dict:
        pk = self.request.data.get('pk')
        field = self.request.data.get('field')
        self.serializer_class.Meta.model = self.model
        self.serializer_class.Meta.fields = [field]
        data = self.model.objects.filter(pk=pk).values(field)
        if len(data) != 0:
            serializer = self.serializer_class(data=data[0])
            serializer.is_valid(raise_exception=True)
            return data
        else:
            return {'message': f'No register in field {field} for pk {pk} in the database.'}