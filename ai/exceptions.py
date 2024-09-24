
class CannotReadAIFile(Exception): 

    def __init__(self, message): 

        super().__init__("Cannot comprehend: " + message)