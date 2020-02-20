# Airbnb clone- The console description


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The project is a command interpreter to manipulate data without a visual interface. The console has prompt (hbnb) and its shown every time a command is executed. In this console you can use different commands as: all, create, destroy, help, quit, show, update and EOF.

## Instructions

### Clone repository
To clone the repository, you must type the following command:
```bash
git clone https://github.com/OscarDRT/AirBnB_clone.git
```
### Execution

To execute the program you must type:
```bash
(./console.py)
```
### Commands

```bash
all: Prints all string representation of all instances based or not on the class name.

create: Creates a new instance.

destroy: Deletes an instance based on the class name and id.

help: Provide the description of the commands.

show: Prints the string representation of an instance based on the class name and id.

update: Updates an instance based on the class name and id by adding or updating attribute.

quit: Exit the program.
```

### Exit
To exit the program, you can use exit quit command.

## Files

```bash
README.md: Description of the repository.

AUTHORS: Authors of the repository.

console.py: File that contains the entry point of the command interpreter.

file.json: File that saves the created instances.

models/base_model.py: Defines all common attributes/methods for other classes.

models/amenity.py: Amenity class inherited from BaseModel.

models/city.py: City class inherited from BaseModel.

models/place.py: Place class inherited from BaseModel.

models/review.py: Review class inherited from BaseModel.

models/state.py: State class inherited from BaseModel.

models/user.py: User class inherited from BaseModel.

models/engine/file_storage: File that serializes instances to a JSON file and deserializes JSON file to instances.

```
## Examples
Examples of different commands:

```bash
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$ ./console.py
(hbnb) create City
06bebff4-cfba-4d8e-9ca5-62e8637a87e8
(hbnb) all
[City] (06bebff4-cfba-4d8e-9ca5-62e8637a87e8) {'created_at': datetime.datetime(2020, 2, 19, 17, 41, 18, 907065), 'updated_at': datetime.datetime(2020, 2, 19, 17, 41, 18, 907135), 'id': '06bebff4-cfba-4d8e-9ca5-62e8637a87e8'}
(hbnb) create User
785b0cb8-c344-4972-b044-3ecce1861b60
(hbnb) all
[City] (06bebff4-cfba-4d8e-9ca5-62e8637a87e8) {'created_at': datetime.datetime(2020, 2, 19, 17, 41, 18, 907065), 'updated_at': datetime.datetime(2020, 2, 19, 17, 41, 18, 907135), 'id': '06bebff4-cfba-4d8e-9ca5-62e8637a87e8'}
[User] (785b0cb8-c344-4972-b044-3ecce1861b60) {'created_at': datetime.datetime(2020, 2, 19, 17, 41, 47, 165330), 'updated_at': datetime.datetime(2020, 2, 19, 17, 41, 47, 165392), 'id': '785b0cb8-c344-4972-b044-3ecce1861b60'}
(hbnb) show User
** instance id missing **
(hbnb) show User 785b0cb8-c344-4972-b044-3ecce1861b60
[User] (785b0cb8-c344-4972-b044-3ecce1861b60) {'created_at': datetime.datetime(2020, 2, 19, 17, 41, 47, 165330), 'updated_at': datetime.datetime(2020, 2, 19, 17, 41, 47, 165392), 'id': '785b0cb8-c344-4972-b044-3ecce1861b60'}
(hbnb) create Place
0e7dbdf4-f805-4fdc-b86a-3dc8e4a8980e
(hbnb) all
[Place] (0e7dbdf4-f805-4fdc-b86a-3dc8e4a8980e) {'created_at': datetime.datetime(2020, 2, 19, 17, 43, 15, 522640), 'updated_at': datetime.datetime(2020, 2, 19, 17, 43, 15, 522736), 'id': '0e7dbdf4-f805-4fdc-b86a-3dc8e4a8980e'}
[City] (06bebff4-cfba-4d8e-9ca5-62e8637a87e8) {'created_at': datetime.datetime(2020, 2, 19, 17, 41, 18, 907065), 'updated_at': datetime.datetime(2020, 2, 19, 17, 41, 18, 907135), 'id': '06bebff4-cfba-4d8e-9ca5-62e8637a87e8'}
[User] (785b0cb8-c344-4972-b044-3ecce1861b60) {'created_at': datetime.datetime(2020, 2, 19, 17, 41, 47, 165330), 'updated_at': datetime.datetime(2020, 2, 19, 17, 41, 47, 165392), 'id': '785b0cb8-c344-4972-b044-3ecce1861b60'}
(hbnb) destroy City 06bebff4-cfba-4d8e-9ca5-62e8637a87e8
(hbnb) all
[Place] (0e7dbdf4-f805-4fdc-b86a-3dc8e4a8980e) {'created_at': datetime.datetime(2020, 2, 19, 17, 43, 15, 522640), 'updated_at': datetime.datetime(2020, 2, 19, 17, 43, 15, 522736), 'id': '0e7dbdf4-f805-4fdc-b86a-3dc8e4a8980e'}
[User] (785b0cb8-c344-4972-b044-3ecce1861b60) {'created_at': datetime.datetime(2020, 2, 19, 17, 41, 47, 165330), 'updated_at': datetime.datetime(2020, 2, 19, 17, 41, 47, 165392), 'id': '785b0cb8-c344-4972-b044-3ecce1861b60'}
(hbnb) update Place 0e7dbdf4-f805-4fdc-b86a-3dc8e4a8980e name Yuli
(hbnb) all
[Place] (0e7dbdf4-f805-4fdc-b86a-3dc8e4a8980e) {'updated_at': datetime.datetime(2020, 2, 19, 17, 44, 22, 537480), 'created_at': datetime.datetime(2020, 2, 19, 17, 43, 15, 522640), 'name': 'Yuli', 'id': '0e7dbdf4-f805-4fdc-b86a-3dc8e4a8980e'}
[User] (785b0cb8-c344-4972-b044-3ecce1861b60) {'created_at': datetime.datetime(2020, 2, 19, 17, 41, 47, 165330), 'updated_at': datetime.datetime(2020, 2, 19, 17, 41, 47, 165392), 'id': '785b0cb8-c344-4972-b044-3ecce1861b60'}
(hbnb)
```

## Authors
Oscar Riaño Tapias- Github: OscarDRT

Yulieth Zuluaga Gómez- Github: yulyzulu
