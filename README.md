# OBP Auth Server

### API Endpoints

All requests are POST requests, and require data to be sent as form data. Parameters for a successful request are listed below.

All requests must be made from an authorized client (server) within the scope of the Application as a whole. Authorized clients must supply their custom Client ID and Client Secret that was supplied by this Auth Server with every request. They must also utilize the Public Key to decode the JWT.

#### Verify Credentials
**Route**: '/authenticate'

**Method**: POST

**Parameters**: 

* Email as 'email' 
* Password as 'password' 
* Client ID as 'client_id' 
* Client Secret as 'client_secret

#### Register User
**Route**: '/register'

**Method**: POST

**Parameters**: 

* Email as 'email' 
* Password as 'password' 
* First Name as'fName' 
* Last Name as 'lName' 
* Client ID as 'client_id' 
* Client Secret as 'client_secret

#### Update Password
**Route**: '/updatepassword'

**Method**: POST

**Parameters**:

* Email as 'email' 
* Old Password as 'oldPassword' 
* New Password as'newPassword 
* Client ID as 'client_id' 
* Client Secret as 'client_secret

#### Delete User
**Route**: '/delete'

**Method**: POST

**Parameters**:
* Email as 'email' 
* Password as 'password' 
* Client ID as 'client_id' 
* Client Secret as 'client_secret