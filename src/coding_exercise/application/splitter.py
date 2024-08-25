from coding_exercise.domain.model.cable import Cable


class Splitter:

    def __validate(self, cable: Cable, times: int):
        if not isinstance(cable, Cable) or not isinstance(times, int):
            raise ValueError("Invalid input types")

        if cable.length < 2 or cable.length > 1024:
            raise ValueError("Cable length out of bounds (2-1024)")

        if times < 1 or times > 64:
            raise ValueError("Number of splits out of bounds (1-64)")

        if times >= cable.length:
            raise ValueError("Number of splits cannot exceed or be equal to cable length")

    def split(self, cable: Cable, times: int) -> list[Cable]:
        # Validate inputs
        self.__validate(cable, times)

        length = cable.length
        num_pieces = times + 1
        piece_length = length // num_pieces
        remainder = length % num_pieces

        result = []

        # Create the cables for the main splits
        for index in range(num_pieces):
            result.append(Cable(piece_length, self.formatName(cable.name, index , num_pieces)))

        # If there's a remainder, split it further
        if remainder > 0:
            # Generate new cables for the remainder
            remaining_length = remainder
            index = num_pieces
            while remaining_length > 0:
                if remaining_length >= piece_length:
                    result.append(Cable(piece_length, self.formatName(cable.name, index, num_pieces)))
                    remaining_length -= piece_length
                else:
                    result.append(Cable(remaining_length, self.formatName(cable.name, index, num_pieces)))
                    remaining_length = 0
                index += 1

        return result

    def formatName(self, name:str, index: int, num_pieces: int) -> str:
        num_pieces_length = f"{num_pieces}".__len__()
        format = f"0{num_pieces_length}d"
        return f"{name}-{index:{format}}"


