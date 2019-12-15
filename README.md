# pctrl REST API v1

[Installation](#Install)

## Overview

For `POST`, `PUT`, `DELETE` requests, all data is sent and received as JSON with a Content-Type of 'application/vnd.api+json' and conform to the [JSON:API](https://jsonapi.org/) specification. For `GET` requests, any parameters not specified as a segment in the path can be passed as an HTTP query string parameter.

Anonymous user can make `a maximum of 20 requests per minute`.

Requests that return multiple items will be paginated to 5 items by default. You can specify further pages with the ?page[number]= parameter or set a custom page size up to 100 with the ?page[size] parameter.

~~Authentication/JWT stuff..~~ (maybe on next sprint)

Swagger documentation is available at swagger/.

## Controls
Below are the attributes of a control. All attributes are required.

| Name              | Type   | Description |
|-------------------|--------|-------------|
| name              | string | The name of the control (e.g. "Single-Qubit Driven"). |
| type              | string | Valid control types are `Primitive, CORPSE, Gaussian, CinBB and CinSK`. |
| maximum_rabi_rate | string | The maximum achievable angular frequency of the Rabi cycle for a driven quantum transition. This is `a number between 0 and 100`. |
| polar_angle       | string | An angle measured from the z-axis on the Bloch sphere. This is `a number between 0 and 1` (units of pi). | 

### Create a new control
```
POST /controls
```

### List all controls
```
GET /controls
```
List all controls ~~that the authenticated user owns.~~ You can also filter the result with query parameters.
#### Parameters
Any of the attribute names. Examples:
```
/controls                               # list all controls
/controls?name=Single-Qubit+Driven      # list controls with name "Single-Qubit Driven"
/controls?name=Single-Qubit+Driven&type=Primitive&maximum_rabi_rate=1&polar_angle=0.34    # list controls that satisfy all the query parameters
```

### Get a specific control
```
GET /controls/:id
```
Fetch a control identified in id. ~~Note that the authenticated user only have access to the controls they own.

### Update a specific control
Update a control identified in id. Note that the control must exist ~~and the authenticated user may only alter the controls they own~~.
```
PUT /controls/:id
```

### Delete a specific control
```
DELETE /controls/:id
```
Delete a control identified in id. Note that the control must exist ~~and the authenticated user may only delete the controls they own~~.

### Bulk upload controls in CSV format
```
POST /controls/csv
```
Bulk upload controls ~~for the authenticated user~~. The CSV file must have the attribute names of a control as header names, and following the constraints on each attribute. A sample CSV file can be found at [sample](https://github.com/qctrl/back-end-challenge/blob/master/assets/controls.csv).

### Download controls in CSV format
```
GET /controls/csv
```
Download all controls ~~ownd by the authenticated user. You can also filter the result with query parameters before downloading to reduce file size~~. A sample CSV file can be found at [sample](https://github.com/qctrl/back-end-challenge/blob/master/assets/controls.csv).

## Installation
```
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

### Connect to your database (PostgreSQL)
Example instructions:
Create a data base called `pctrl`, then create a user named`pctrluser`, then grant all priviledges on database `pctrl` to `pctrluser`.

In q_ctrl_api/settings.py:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pctrl',
        'USER': 'pctrluser',
        'PASSWORD': 'sample_password',
        'HOST': 'localhost',
        'PORT': '',
        'TEST': {
            'NAME': 'test_controls',
        },
    }
}
```
