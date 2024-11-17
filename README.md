# PostgreSQL Query Manager with GUI Interface
This project implements a Graphical User Interface (GUI) application using Tkinter that allows users to interact with a PostgreSQL database. It provides features to log in with credentials, execute SQL queries, and display query results in a user-friendly format. The interface is designed to be intuitive and visually appealing, utilizing themes and modern design elements.

## Key Features
### 1. User Authentication:
The first page provides a login form where users enter their username and password.
Validates credentials and transitions to the main query editor if login succeeds.

### 2. Query Execution:
The second page contains a Query Editor where users can input and run SQL queries.
Results from executed queries are fetched from the database and displayed in a text area.

### 3. Customizable UI:
Utilizes ttkthemes for modern theme support.
Includes custom images (e.g., login buttons, background images) to enhance aesthetics.
Responsive design ensures proper alignment and centering on different screen sizes.

### 4. Integration with PostgreSQL:
Leverages Psycopg2, a Python library for connecting to PostgreSQL databases.
Executes SQL queries securely using a database cursor.
Provides an example query (SELECT * FROM "TABLE NAME") for ease of use.

### 5. Additional Features:
The second page includes scrollbars for navigating large query results.
The application is designed with transparency and always-on-top options for convenience.
Uses a placeholder for the database icon to represent the query tool.

## Implementation Details
### Technologies Used
- Tkinter: For GUI development.
- ttkthemes: To enhance the default Tkinter widgets with modern themes.
- Psycopg2: For interacting with the PostgreSQL database.
- Pillow: For handling and resizing images.
- OS Module: For managing file paths and system-level configurations.

### Workflow
**1. Login Page:**
Displays input fields for username and password.
Validates credentials through the get_info function (logic placeholder).
**2. Query Page:**
Displays a query editor with an input text box for SQL queries.
Includes a "Run" button to execute queries via the get_query function.
Fetches and displays query results in the output text area with proper scroll support.
**3. Database Connection:**
Connects to PostgreSQL using Psycopg2 (connection setup code omitted but implied).
Executes queries through a database cursor and fetches results.
