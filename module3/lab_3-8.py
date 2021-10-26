# create script with creating new file object
# Open it with name myfile.txt and mode “w”
file = open('myfile.txt', 'w')
# Write into file string "Hello file world!"
file.write("Hello file world!")
# Close file
file.close()
# Create file object for above file with mode “r+”
file = open('myfile.txt','r+')
# Read and print file content
print(file.read())
# Move to string position after Hello and set new value here
file.seek(len("Hello "))
file.write("new " + "value" + " !")
# Save file with flush method
file.flush()
# Answer on the questions how embedded data structures works, i.e. list as a value of dictionary.