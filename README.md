# nucleo
A django app for building social networks (at the core of Naible services)


# Examples

> cd samples/g0ph  

A simple social network application.


## Install packages
> sudo pip install -r requirements.txt 

## Running in Django

> cd samples/g0ph  
> python manage.py migrate  
> \# Optionally you want to create a super user:  
> python manage.py createsuperuser  
> python manage.py runserver  

# Angular

For now we use a bit outdated grunt scripting. Good news that django 
is properly configured to serve the developers version.

The usual angular structure can be found in `samples/g0ph/g0ph/ng-app`.

First, build dependencies:

> cd samples/g0ph/g0ph   
> sudo npm install  
> bower install  

# License

	Unless otherwise specified every source code file in this repository 
	is a part of *Naible nucleo* software. Naible nucleo is free software: you can redistribute it and/or modify it under the terms of the [GNU General Public License](https://github.com/Naible/django-nucleo/blob/master/LICENSE) as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program.  If not, see <http://www.gnu.org/licenses/>.
