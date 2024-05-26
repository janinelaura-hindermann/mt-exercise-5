import os
from ruamel.yaml import YAML


def create_beam_size_configs(input_file, output_dir, beam_sizes):
    yaml = YAML()

    # Load the original YAML file
    with open(input_file, 'r') as file:
        config = yaml.load(file)

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Create copies with different beam sizes
    for beam_size in beam_sizes:
        # Update the beam_size in the configuration
        config['testing']['beam_size'] = beam_size

        # Define the new filename
        new_filename = os.path.join(output_dir, f'bpe_5000_beam_{beam_size}.yaml')

        # Save the new configuration to a new YAML file
        with open(new_filename, 'w') as new_file:
            yaml.dump(config, new_file)

        print(f'Created {new_filename} with beam_size {beam_size}')


if __name__ == '__main__':
    # Parameters
    input_file = '../configs/bpe_5000.yaml'
    output_dir = '../configs/bpe_5000_beam_size'
    beam_sizes = range(1, 11)

    # Call the function
    create_beam_size_configs(input_file, output_dir, beam_sizes)
