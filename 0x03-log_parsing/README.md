# Alx Interview - Log Parsing

## Description

This project focuses on learning how to read data from the terminal (standard input), extract useful information from it, and calculate certain metrics. You will write a Python script called `0-stats.py` that reads log data from standard input. The job of the script is to parse the input and calculate certain metrics. The log data follows a particular format, and your script needs to process each entry to calculate two key metrics: **Total File Size**: This tracks the cumulative size of all files mentioned in the log entries. **Status Code Counts:** This counts how many times each status code (such as 200, 404, etc.) appears in the log data. In the end, you will be able to calculate and display these metrics based on the log entries provided to your script.

## Project Structure

| Task                        | Description                                                                                                                                       | Source Code     |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| Log Parsing (mandatory)     | Write a script that reads stdin line by line and computes metrics: <br> Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>` (if the format is not this one, the line must be skipped). <br> After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning: <br> - Total file size: File size: `<total size>` <br> - Number of lines by status code: possible status code: 200, 301, 400, 401, 403, 404, 405 and 500. <br> Status codes should be printed in ascending order. | [0-stats.py](./0-stats.py) |


## Environment

- Ubuntu 20.04 LTS
- python3 (version 3.4.3)
- PEP 8 style (version 1.7.x)

## Requirements

- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- Your code should use the PEP 8 style (version 1.7.x)
- All your files must be executable
- The length of your files will be tested using wc

## Learning Objectives

- Understand file I/O in Python.
- Parse and process log data efficiently.
- Handle keyboard interruptions gracefully.
- Utilize dictionaries for data aggregation.

## Prototypes Used in the Project

| Function          | Description                                                                                  |
|-------------------|----------------------------------------------------------------------------------------------|
| `parse_log_line`  | Parses a single line of log data and updates the total size and status code counts.         |
| `print_summary`   | Outputs the current total size and count of status codes.                                   |
| `signal_handler`  | Handles keyboard interruptions to allow graceful exits.                                     |

## How to use

- **Define a Function to Handle Input**: Read lines from stdin in a loop.
- **Parse Each Line**: Use regular expressions to extract fields like status code and file size.
- **Store Data in a Dictionary**: Count status codes and accumulate file sizes.

```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```

1. **Generate Sample Logs**: You can use the provided `0-generator.py` script to simulate log entries. Run it in the terminal:

```bash
#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    ))
    sys.stdout.flush()

alexa@ubuntu:~/0x03-log_parsing$ ./0-generator.py | ./0-stats.py 
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
File size: 16305
200: 3
301: 3
400: 4
401: 2
403: 5
404: 5
405: 4
500: 4
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
Traceback (most recent call last):
  File "./0-stats.py", line 15, in <module>
Traceback (most recent call last):
  File "./0-generator.py", line 8, in <module>
    for line in sys.stdin:
KeyboardInterrupt
    sleep(random.random())
KeyboardInterrupt
```

2. **Pipe the Generated Logs to the Stats Script**: Use a pipe to send the output of the generator to the log parsing script:

   ```bash
   ./0-generator.py | ./0-stats.py
   ```
- Ensure that both `0-generator.py` and `0-stats.py` are executable:

   ```bash
   chmod +x 0-generator.py 0-stats.py
   ```

3. **Keyboard Interruption**: You can stop the execution at any time using `CTRL + C`, which will also print the current statistics before exiting.

- **Testing**: Test your script with various log formats to ensure it handles different cases.


### Additional Notes
- **Understand file I/O in Python**: Learn how to read and write data using Python's file handling capabilities, including reading from standard input.
- **Parse and process log data efficiently**: Extract and analyze specific information from log entries while optimizing the process for speed and performance.
- **Handle keyboard interruptions gracefully**: Implement mechanisms to capture and manage interruptions (like `Ctrl+C`) to ensure a smooth exit without data loss.
- **Utilize dictionaries for data aggregation**: Use Python dictionaries to store and count occurrences of status codes and other metrics for easy access and manipulation.

- **File I/O(Reading Input)**: Read from `sys.stdin` and handle input efficiently. Use `sys.stdin` to read log entries line by line
- **Parsing Data**: Extract specific fields from each log entry.
- **Aggregating Results**: Count occurrences of status codes and accumulate file sizes.
- **Handling Exceptions**: Manage potential errors during input and processing.

- **Signal Handling**: Allow for graceful shutdown of the program (e.g., on CTRL + C).
- **Data Processing**: Understand how to parse strings and aggregate data.
- **Regular Expressions**: Validate and extract specific patterns from the logs.
- **Dictionaries**: Use to count occurrences and summarize data.
- **Exception Handling**: Implement to ensure robustness of the code.


## Tasks

0. **Log parsing**
**File:** 0-stats.py
Write a script that reads stdin line by line and computes metrics:

Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>` (if the format is not this one, the line must be skipped)

After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:

- Total file size: File size: `<total size>`  
  where `<total size>` is the sum of all previous `<file size>` (see input format above)
  
- Number of lines by status code:  
  possible status code: 200, 301, 400, 401, 403, 404, 405 and 500  
  if a status code doesn’t appear or is not an integer, don’t print anything for this status code  
  format: `<status code>: <number>`  
  status codes should be printed in ascending order

Warning: In this sample, you will have random value - it’s normal to not have the same output as this one.
```python
alexa@ubuntu:~/0x03-log_parsing$ cat 0-generator.py
#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    ))
    sys.stdout.flush()

alexa@ubuntu:~/0x03-log_parsing$ ./0-generator.py | ./0-stats.py 
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
File size: 16305
200: 3
301: 3
400: 4
401: 2
403: 5
404: 5
405: 4
500: 4
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
Traceback (most recent call last):
  File "./0-stats.py", line 15, in <module>
Traceback (most recent call last):
  File "./0-generator.py", line 8, in <module>
    for line in sys.stdin:
KeyboardInterrupt
    sleep(random.random())
KeyboardInterrupt
alexa@ubuntu:~/0x03-log_parsing$ 
```
