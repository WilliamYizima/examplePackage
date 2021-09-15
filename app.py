from examplePackage import SerializerFactory, TargetServiceBuilder

factory = SerializerFactory()
a = factory.register('PANDORA', TargetServiceBuilder())


payload01 = {
    'status':'estado',
    'event':'evento',
    'created_at':'data_criacao'
}

pandara = factory.create('PANDORA', **payload01)

payload02 = {
    'status':'state',
    'event':'name-event',
    'created_at':'date'
}

c = factory.register('P', TargetServiceBuilder())
p = factory.create('P', **payload02)

request01 = {
    'estado':'done',
    'evento':'doido',
    'data_criacao':'11-09-2019'
}

print(pandara.serializer(request01))