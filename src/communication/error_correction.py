import logging
import numpy as np

class ErrorCorrection:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)

    def hamming_code(self, data):
        """
        Encodes 4 bits of data using Hamming (7,4) code.
        :param data: A string of 4 bits (e.g., '1011').
        :return: A numpy array of encoded data (7 bits).
        """
        data_bits = np.array(list(map(int, data)), dtype=int)
        if len(data_bits) != 4:
            logging.error("Data must be 4 bits long for Hamming (7,4) code.")
            return None

        # Calculate parity bits
        p1 = data_bits[0] ^ data_bits[1] ^ data_bits[3]  # Parity bit for positions 1, 2, 4
        p2 = data_bits[0] ^ data_bits[2] ^ data_bits[3]  # Parity bit for positions 1, 3, 4
        p3 = data_bits[1] ^ data_bits[2] ^ data_bits[3]  # Parity bit for positions 2, 3, 4

        # Create encoded data
        encoded_data = np.array([data_bits[0], data_bits[1], p1, data_bits[2], p2, data_bits[3], p3])
        logging.info(f"Encoded data: {encoded_data}")
        return encoded_data

    def detect_and_correct(self, received_data):
        """
        Detects and corrects a single-bit error in the received data using Hamming (7,4) code.
        :param received_data: A numpy array of received data (7 bits).
        :return: A numpy array of corrected data (4 bits).
        """
        if len(received_data) != 7:
            logging.error("Received data must be 7 bits long.")
            return None

        # Calculate parity bits
        p1 = received_data[0] ^ received_data[1] ^ received_data[3] ^ received_data[6]
        p2 = received_data[0] ^ received_data[2] ^ received_data[3] ^ received_data[5]
        p3 = received_data[1] ^ received_data[2] ^ received_data[3] ^ received_data[4]

        # Determine error position
        error_position = p1 * 1 + p2 * 2 + p3 * 4
        if error_position != 0:
            logging.warning(f"Error detected at position: {error_position}. Correcting...")
            received_data[error_position - 1] ^= 1  # Correct the error

        logging.info(f"Corrected data: {received_data}")
        return received_data[:4]  # Return the original 4 bits of data

# Example usage
if __name__ == "__main__":
    error_correction = ErrorCorrection()

    # Example data to encode
    data_to_encode = "1011"
    encoded_data = error_correction.hamming_code(data_to_encode)

    # Simulate a transmission error (flip the first bit)
    received_data = np.copy(encoded_data)
    received_data[0] ^= 1  # Introduce an error
    logging.info(f"Received data with error: {received_data}")

    # Detect and correct the error
    corrected_data = error_correction.detect_and_correct(received_data)
    logging.info(f"Final corrected data: {corrected_data}")
