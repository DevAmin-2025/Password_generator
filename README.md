# Password Generator
This project contains a password generator application written in Python. The generator can create three types of passwords:

1. Pin Codes
2. Random Passwords
3. Memorable Passwords

## How It Works
The password generator uses the Python `random` module to generate passwords based on user preferences. The generator is split into three classes, each representing a different type of password generation:

1. `PinCodeGenerator` creates a numeric password of a specified length.
2. `RandomPasswordGenerator` generates a completely random password of a specified length, optional with numbers, and symbols.
3. `MemorablePasswordGenerator` creates a password made up of a set number of randomly chosen words. It can optionally separate the words with a separator.

Each generator class inherits from a base `PasswordGenerator` class. They each override the base class's `generate()` method in order to provide their own unique password generation functionality.

## Running the Project
1. You can clone the repository, set your PYTHONPATH, navigate to the project directory and run the project using Python:

    **Clone the Repository**: Open your terminal and run the following command to clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repo.git
    ```
    Replace your-username and your-repo with the actual GitHub username and repository name.

    ```bash
    export PYTHONPATH="${PYTHONPATH}:/your/path/to/main/directory"
    python src/main.py
    ```
    Be sure to replace `/your/path/to/main/directory` with the actual path to the directory containing your project.

2. Install any necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```
