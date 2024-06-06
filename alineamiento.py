import argparse
import re 
from utils.file_io import read_dna_sequence
from utils.validators import validate_dna_sequence
from utils.validators import validate_fasta_format
from utils.validators import check_sequence_length
from operations.marcos_lectura import coincidencias

def main():
    parser = argparse.ArgumentParser(description="Lee archivo de entrada y salida.")
    parser.add_argument("-i_1", "--input_file_1", type=str, required=True, help="El primer archivo de texto que quieres procesar.")
    parser.add_argument("-i_2", "--input_file_2", type=str, required=True, help="El segundo archivo de texto que quieres procesar.")
    parser.add_argument("-o", "--output_file", type=str, default="out.txt", help="El archivo ddonde se guarda la salida 'out.txt' por defecto.")
    args = parser.parse_args()
    try:
        file_1 = read_dna_sequence(args.input_file_1)
        file_2 = read_dna_sequence(args.input_file_2)
    except IOError as ex: 
        print(f"Error al leer archivos: {ex}")

    if validate_fasta_format(args.input_file_1) and validate_fasta_format(args.input_file_2):

        try:
            with open(args.input_file_1, 'r') as archivo: 
                secuencia_1 = archivo.read()
        
            with open(args.input_file_2, 'r') as archivo: 
                secuencia_2 = archivo.read()

        except IOError as ex:
            print("Lo siento, los archivos no se pudieron encontrar: {ex}")

        secuencias_nucleotidos_1 = re.findall(r'[ACTG]', secuencia_1)
        secuencias_nucleotidos_1 = ''.join(secuencias_nucleotidos_1)
        print(secuencias_nucleotidos_1)

        secuencias_nucleotidos_2 = re.findall(r'[ACTG]', secuencia_2)
        secuencias_nucleotidos_2 = ''.join(secuencias_nucleotidos_2)
        print(secuencias_nucleotidos_2)

        if validate_dna_sequence(secuencias_nucleotidos_1) == True and validate_dna_sequence(secuencias_nucleotidos_2)== True:
        
            if check_sequence_length(secuencias_nucleotidos_1, min_length=100) == True and check_sequence_length(secuencias_nucleotidos_2, min_length=100) == True:

                interseccion=secuencias_nucleotidos_1 and secuencias_nucleotidos_2
                print(f"La secuencia en común es: {interseccion}")

                coincidencias(secuencias_nucleotidos_1, secuencias_nucleotidos_2)

if __name__ == "__main__":
    main()