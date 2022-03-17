from antlr4.error.ErrorStrategy import *


class ErrorHandeling(BailErrorStrategy):

    def recover(self, recognizer:Parser, e:RecognitionException):
        context = recognizer._ctx
        while context is not None:
            context.exception = e
            context = context.parentCtx
        raise ParseCancellationException(e)
        exit()

    # Make sure we don't attempt to recover inline; if the parser
    #  successfully recovers, it won't throw an exception.
    #
    def recoverInline(self, recognizer:Parser):
        self.recover(recognizer, InputMismatchException(recognizer))
        exit()


    # Make sure we don't attempt to recover from problems in subrules.#
    def sync(self, recognizer:Parser):
        pass