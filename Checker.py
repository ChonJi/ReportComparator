from Parser import Parser


class Checker:

    artifact_id = 144070184

    def __init__(self):
        parser = Parser(self.artifact_id)
        for element in parser.compare_failures():
            print('New test failed: ' + element)

if __name__ == "__main__":
    Checker()



