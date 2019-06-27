# OBP Auth Server

### API Endpoints

All requests are POST requests, and require data to be sent as form data. Parameters for a successful request are listed below.

All requests must be made from an authorized client (server) within the scope of the Application as a whole. Authorized clients must supply their custom Client ID and Client Secret that was supplied by this Auth Server with every request. They must also utilize the Public Key to decode the JWT.


### Verify Credentials
**Route**: '/authenticate'

**Method**: POST

**Parameters**: 

* Email as 'email' 
* Password as 'password' 
* Client ID as 'client_id' 
* Client Secret as 'client_secret

**Response**
* 200 - OK
    ```
    {
        access_token: access_token value,
        token_type: 'jwt'
        expires_in: expiration time,
        firstName: user First Name,
        lastName: user Last Name
    } 
    ```
* 400 - Bad Request
    ```
    {
        "error": "Access Denied - invalid request"
    }
    ```
* 401 - Unauthorized
    ```
    {
        "error": "Access Denied - client not authorized"
    }
    ```
* 401 - Unauthorized
    ```
    {
        "error": "Access Denied - invalid credentials"
    }
* 500 - Internal Server Error
    ```
    {
        'error': 'Error Connecting to DB'
    }
    ```

### Register User
**Route**: '/register'

**Method**: POST

**Parameters**: 

* Email as 'email' 
* Password as 'password' 
* First Name as'fName' 
* Last Name as 'lName' 
* Client ID as 'client_id' 
* Client Secret as 'client_secret

**Response**
* 200 - OK 
    ```
    {
        access_token: access_token value,
        token_type: 'jwt'
        expires_in: expiration time,
        firstName: user First Name,
        lastName: user Last Name
    } 
    ```
* 400 - Bad Request
    ```
    {
        "error": "Access Denied - invalid request"
    }
    ```
* 401 - Unauthorized
    ```
    {
        "error": "Access Denied - client not authorized"
    }
    ```
* 401 - Unauthorized
    ```
    {
        "error": "This email already exists in the DB"
    }
* 500 - Internal Server Error
    ```
    {
        'error': 'Error Connecting to DB'
    }
    ```


### Update Password
**Route**: '/updatepassword'

**Method**: POST

**Parameters**:

* Email as 'email' 
* Old Password as 'oldPassword' 
* New Password as'newPassword 
* Client ID as 'client_id' 
* Client Secret as 'client_secret


### Delete User
**Route**: '/delete'

**Method**: POST

**Parameters**:
* Email as 'email' 
* Password as 'password' 
* Client ID as 'client_id' 
* Client Secret as 'client_secret