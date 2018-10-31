import json


class InformationFromOpencvToPi:
    function = 'test'
    direction = 'camera to server'
    cameraOK = False
    ignitorFlamed = False
    ignitorFlameLength = 0
    specimenLength = 0
    firstDistanceBetweenSpecimenAndIgnitor = 0
    secondDistanceBetweenSpecimenAndIgnitor = 0
    specimenFlamed = False
    specimenFlameLength = 0
    specimenBurnoffLength = 0
    specimenBurnTime = 0

    def serialize_object(self,obj):
        d = {'__classname__': type(obj).__name__}
        d.update(vars(obj))
        return d

    def unserialize_object(self, d):
        clsname = d.pop('__classname__', None)
        if clsname:
            cls = classes[clsname]
            obj = cls.__new__(cls)  # Make instance without calling __init__
            for key, value in d.items():
                setattr(obj, key, value)
            return obj
        else:
            return d