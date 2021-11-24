class Filter:
    def __init__(self, request, serializer_class, model):
        self.request = request
        self.serializer_class = serializer_class
        self.model = model

    def filter(self) -> dict:
        pk = self.request.data.get('user_id')
        field = self.request.data.get('field')
        if type(field) is list:
            self.serializer_class.Meta.fields = field
        else:
            self.serializer_class.Meta.fields = [field]
        self.serializer_class.Meta.model = self.model
        serializer = self.serializer_class(self.model.objects.filter(pk=pk), many=True)
        return serializer.data
