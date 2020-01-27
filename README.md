# datasciencemaster_effectofiot

These python files are part of my masterthesis to analyze 8.700 JSON files.

1. First I deleted with (delete_json_objects.py) all files that had none values in it

2. Next I had to determine the factors for my later cluster analysis. Because of the original size of my JSON files 
I wanted to change them and replace them with the new factors. So I only have the data that is relevant for me per JSON file.

3. After I only had the JSON files with my factors, I had to check if the JSON files were in the right format (find_false.json).

4. Then I had to find the outliers from my data sets and replace the values which are illogical with the mean values.
