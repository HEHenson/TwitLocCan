# TwitLocCan

Ecletic Routines for Categorizing Location Information Given on Social Media (Primarily Twitter) 

## Installation
Pip install not working yet.  At this point, I am uploading the files.  Will reoganize when I have enough for a test install.

```bash
$ pip install twitloccan
```

## Usage

`twitloccan` provides a set of tools to convert a text field describing location to a categorical variable.
Sample usage could be:

```python
import location
import geograpy
testlocation = location.C3(useGEOGRPY = True)
isCan = testlocation.isCan("Winnipeg")

print(isCan)
```

## Contributing

Contributions are welcome.  Check out the guidelines.  Bonus points for those familiar with
Canadian Privacy Guidelines.  Please note that this project is release with a Code of Conduct.
By contributing to this project, you agree to abide by its terms.

## License

`twitloccan` was created by Harold Henson. It is licensed under the terms of the MIT
license.

