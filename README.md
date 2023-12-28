[![linter-run](https://github.com/yuriy-kormin/territory_sectors/actions/workflows/linter-run.yml/badge.svg)](https://github.com/yuriy-kormin/territory_sectors/actions/workflows/linter-run.yml)
[![test](https://github.com/yuriy-kormin/territory_sectors/actions/workflows/django-test.yml/badge.svg)](https://github.com/yuriy-kormin/territory_sectors/actions/workflows/django-test.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/9c7062dd68f9f445a56e/maintainability)](https://codeclimate.com/github/yuriy-kormin/territory_sectors/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/9c7062dd68f9f445a56e/test_coverage)](https://codeclimate.com/github/yuriy-kormin/territory_sectors/test_coverage)

# Territory Sector Manager

Application designed to simplify the process of marking locations on a map using markers.

## Features

- Map Marking: Easily mark locations on the map using markers.
- Hierarchy: Organize locations into apartments, houses, and sectors.
- Spatial Logic: Determine the sector of a house based on the intersection of its GPS coordinates 
with the polygon defining the sector boundaries.
- Security. App employs Certbot to ensure a secure and encrypted connection through HTTPS. 
This implementation guarantees that the communication between users and the Territory Sector Manager server 
- remains confidential and protected. By integrating Certbot, we prioritize the privacy and safety of our users' data, reinforcing our commitment to delivering a secure and reliable mapping experience. 

## Logic

The application revolves around three main entities: apartments, houses, and sectors.

Apartments: Individual living spaces that are part of a house.
Houses: Grouped into sectors and have GPS-tagged addresses and descriptions.
Sectors: Drawn on the map as polygons of any shape, defining the boundaries for grouped houses.


The spatial logic is implemented using the INTERSECTS function in a PostgreSQL extension.
This function allows the app to efficiently determine the sector to which a house belongs by 
checking the intersection of its GPS coordinates with the sector's boundary polygon.

## Future Plans
#### 1. Frontend Enhancement with React
We are actively working on implementing a sleek and interactive frontend using React. 
This enhancement is geared towards providing users with a visually appealing interface, 
making the process of marking locations on the map more intuitive and enjoyable.

#### 2. GraphQL Integration with urql Library
To optimize communication between the frontend and backend, we are exploring the integration of 
GraphQL with the urql library. This combination aims to streamline data queries and updates,
ensuring a seamless and efficient exchange of information between the user interface and the server.

[Here](https://github.com/yuriy-kormin/graphene_react) you can find my initial attempt to kickstart 
this work.


#### Get Involved!
If you are passionate about continuous improvement and want to contribute to the ongoing development 
of this logic, your efforts will be highly appreciated!
We welcome contributors to join us on this journey to create an even more robust and user-friendly
Territory Sector Manager.
Feel free to reach out if you have ideas, suggestions, or if you'd like to get involved in
implementing these exciting features. Together, let's make marking locations on the map a seamless 
and enjoyable experience for everyone!

## Getting Started

To set up the Territory Sector Manager, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yuriy-kormin/territory_sectors
   ```
2. **Install Dependencies**
   ```bash
    make install
   ```
3. **Start the Server**
    ```bash
   make start
   ```
Launch the server on localhost:8000 to begin exploring and utilizing Territory Sector Manager. 
Access the application through your web browser and start marking locations on the map effortlessly.


Contributions are welcome! If you have suggestions, bug reports, or feature requests, 
please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

## Contact

For inquiries, reach out me at [email](yuriy.kormin@gmail.com).

Thank you for using Territory Sector Manager! Happy mapping!