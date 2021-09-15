from examplePackage import SerializerFactory, TargetServiceBuilder

factory = SerializerFactory()
a = factory.register('zapdos', TargetServiceBuilder())


payload01 = {
    'status':'estado',
    'event':'evento',
    'created_at':'data_criacao'
}

tester = factory.create('zapdos', **payload01)

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

print(tester.serializer(request01))