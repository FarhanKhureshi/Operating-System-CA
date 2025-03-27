# Disk Scheduling Algorithm Visualizer

This project is a web application built using Flask that visualizes different disk scheduling algorithms. It allows users to input a sequence of disk requests, a starting head position, and select an algorithm. The application then calculates and displays the total seek count, average seek time, and the sequence of head movements for the chosen algorithm.

## Features

* **Algorithm Selection:** Supports First-Come, First-Served (FCFS), Shortest Seek Time First (SSTF), SCAN, and C-SCAN disk scheduling algorithms.
* **Input Flexibility:** Allows users to input a comma-separated list of disk requests and specify the initial head position.
* **Visualization:** Displays the calculated total seek count, average seek time, and the sequence of head movements.
* **User-Friendly Interface:** Provides a simple and intuitive web interface for easy interaction.

## Technologies Used

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python, Flask
* **Data Transfer:** JSON

## Setup and Installation

1.  **Clone the repository:** `git clone <repository_url> && cd disk-scheduling-visualizer`
2.  **Create a virtual environment (recommended):** `python -m venv venv && source venv/bin/activate` (On Windows, use `venv\Scripts\activate`)
3.  **Install the dependencies:** `pip install Flask`
4.  **Run the application:** `python app.py`
5.  **Open your web browser and navigate to** `http://127.0.0.1:5000/`.

## How to Use

1.  **Enter Disk Requests:** In the "Disk Requests" field, enter the sequence of disk requests separated by commas (e.g., `98,183,37,122,14,124,65,67`).
2.  **Enter Start Position:** In the "Start Position" field, enter the initial position of the disk head (e.g., `53`).
3.  **Select Algorithm:** Choose the desired disk scheduling algorithm from the dropdown menu (FCFS, SSTF, SCAN, C-SCAN).
4.  **Specify Maximum Track (for SCAN and C-SCAN):** If you selected SCAN or C-SCAN, enter the maximum track number of the disk.
5.  **Select Direction (for SCAN and C-SCAN):** If you selected SCAN or C-SCAN, choose the initial direction of the head movement (Left or Right).
6.  **Click "Calculate":** The application will process the input and display the results below the form.

## Output

The application will display the following output:

* **Total Seek Count:** The total number of tracks the disk head moved.
* **Average Seek Time:** The average number of tracks moved per request.
* **Head Movements:** The sequence of track numbers the disk head visited.

## Algorithm Details

The application implements the following disk scheduling algorithms:

| Algorithm | Description                                                                                                                                                                                          |
| :-------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| FCFS      | Processes requests in the order they arrive. Simple to implement but may result in large seek times.                                                                                                    |
| SSTF      | Selects the request closest to the current head position. Aims to minimize seek time but can lead to starvation for requests far from the current position.                                            |
| SCAN      | The disk head moves in one direction, servicing requests along the way. When it reaches one end of the disk, it reverses direction and continues servicing.                                         |
| C-SCAN    | Similar to SCAN, but after reaching one end, the head immediately returns to the other end without servicing any requests. This provides a more uniform waiting time compared to SCAN.               |

## Tables

### Input Parameters

| Field          | Description                                                                 | Example                       |
| :------------- | :-------------------------------------------------------------------------- | :---------------------------- |
| Disk Requests  | Comma-separated sequence of disk request track numbers.                     | `98,183,37,122,14,124,65,67` |
| Start Position | The initial position of the disk head.                                      | `53`                          |
| Algorithm      | The disk scheduling algorithm to use (FCFS, SSTF, SCAN, C-SCAN).             | `SSTF`                        |
| Max Track      | The maximum track number on the disk (required for SCAN and C-SCAN).        | `199`                         |
| Direction      | The initial direction of the head movement (Left or Right, for SCAN/C-SCAN). | `Left`                        |

### Output Results

| Field            | Description                                           | Example       |
| :--------------- | :---------------------------------------------------- | :------------ |
| Total Seek Count | The total number of tracks the disk head moved.       | `640`         |
| Average Seek Time| The average number of tracks moved per request.       | `80.0`        |
| Head Movements   | The sequence of track numbers the disk head visited. | `[53, 65, ...]` |

## Contributing

We welcome contributions! If you'd like to contribute to this project, please follow these steps:

1.  **Fork the repository** on GitHub.
2.  **Clone your forked repository** to your local machine:
    ```bash
    git clone [https://github.com/YOUR_GITHUB_USERNAME/disk-scheduling-visualizer.git](https://github.com/YOUR_GITHUB_USERNAME/disk-scheduling-visualizer.git)
    cd disk-scheduling-visualizer
    ```
3.  **Add the original repository as an upstream remote:**
    ```bash
    git remote add upstream [https://github.com/ORIGINAL_REPO_USERNAME/disk-scheduling-visualizer.git](https://github.com/ORIGINAL_REPO_USERNAME/disk-scheduling-visualizer.git)
    ```
4.  **Create a new branch** for your feature or bug fix:
    ```bash
    git checkout -b feature-name
    ```
5.  **Make your changes and commit them:**
    ```bash
    git add .
    git commit -m "Add your descriptive commit message"
    ```
6.  **Push your changes to your fork:**
    ```bash
    git push origin feature-name
    ```
7.  **Create a pull request** on the original repository.

### Contributors
* **Farhan Khureshi**
* **Prince panchal**
* **Keshav Raj**

## Future Improvements

* **Graphical Visualization:** Implement a graphical representation of the disk head movement to make the algorithms easier to understand visually. This could involve using libraries like `matplotlib` in Python to generate charts or using JavaScript libraries on the frontend.
* **More Algorithms:** Add support for other disk scheduling algorithms such as LOOK, C-LOOK, and optimization-based algorithms like Genetic Algorithms or Ant Colony Optimization.
* **Performance Analysis:** Include features to compare the performance of different algorithms for the same set of requests, possibly by displaying metrics side-by-side or generating comparative reports.
* **Customizable Disk Characteristics:** Allow users to input parameters like the number of cylinders and the speed of the disk to get more realistic seek time calculations.
* **Error Handling and Input Validation:** Implement more robust error handling and input validation to guide users in providing correct input and prevent application crashes.
* **User Interface Enhancements:** Improve the user interface with better styling, responsiveness for different screen sizes, and potentially more interactive elements.
* **Persistence:** Allow users to save and load sets of disk requests and configurations.
* **Testing:** Implement unit and integration tests to ensure the reliability and correctness of the application, especially the algorithm implementations.
* **Deployment:** Explore options for deploying the application to a wider audience, such as using platforms like Heroku, AWS, or Docker.

## License

[MIT License](LICENSE)





