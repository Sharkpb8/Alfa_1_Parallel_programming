#error for Node
class DataTypeError(Exception):
    pass
class DataLenghtError(Exception):
    pass
class DistanceTypeError(Exception):
    pass
class DistanceLenghtError(Exception):
    pass
class NextNodeError(Exception):
    pass
class PrevNodeError(Exception):
    pass

#errors for Linkedlist
class HeadError(Exception):
    pass
class TailError(Exception):
    pass
class NodeError(Exception):
    pass
class DuplicateStationError(Exception):
    pass

#errors for Train
class TypeTypeError(Exception):
    pass
class TrainTypeError(Exception):
    pass 
class TrainNumberTypeError(Exception):
    pass
class TrainNumberLenghtError(Exception):
    pass
class TracksTypeError(Exception):
    pass
class SpeedTypeError(Exception):
    pass
class SpeedError(Exception):
    pass
class CapacityTypeError(Exception):
    pass
class CapacityError(Exception):
    pass
class FuelError(Exception):
    pass
class ConsumptionError(Exception):
    pass
class FuelTypeError(Exception):
    pass
class ConsumptionTypeError(Exception):
    pass
class TravelTypeError(Exception):
    pass
class PassangerTypeError(Exception):
    pass
class TrainTypeError(Exception):
    pass
class EmptyInputError(Exception):
    pass
class LowFuelError(Exception):
    pass
class NotReachableStationError(Exception):
    pass

#errors for main
class ChoiceError(Exception):
    pass
class FormatError(Exception):
    pass

#errors for config
class ConfigDictionaryError(Exception):
    pass
class ConfigListError(Exception):
    pass
class ConfigTrainTypeError(Exception):
    pass
class ConfigSimulationDataError(Exception):
    pass