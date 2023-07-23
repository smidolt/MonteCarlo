## Investment Data Converter

The Investment Data Converter is a Python script designed to convert investment data from a CSV file into a readable format for our Monte Carlo simulations.

### How it Works

1. The script reads the investment data from a CSV file specified as "WRITE_NAME_OF_YOUR_CSV.csv".

2. It removes commas from the "Price" column and converts the values to floating-point numbers.

3. The script rounds the converted prices to integers for better readability.

4. Finally, it saves the modified data into a new CSV file named "new_file.csv".

### Purpose

The Investment Data Converter is essential for preprocessing investment data obtained from a website or other sources. By converting the data into a more suitable format, it prepares the data for use in our Monte Carlo simulations, where accurate and properly formatted data is crucial for meaningful results.

To use the converter, replace "WRITE_NAME_OF_YOUR_CSV.csv" with the actual filename of your investment data in CSV format. After running the script, you will get a new CSV file with the processed data ready for further analysis and simulations.

