"""
NOTE==
        w  ==(write mode)  ===  write mode empty the file if file alrady exist
        a  ==(append mode) ===  append mode don't empty the file
        f.write() function returns number of charater it wrote
          
"""
f=open("text file2.txt","w")             #we open (or create if not already present even if it already present it will replace the content with empty file) new file here with write mode means new file get created 
f.write("is this really a real world?")

f=open("text file3.txt","a")     # we opened the file here with append mode means we can add content at the end of the file(if there is any existing file it don't get truncated) it also create file if not already present
f.write("\nlearn form other person mistakes")


a=f.write("\nlearn form other person mistakes") #f.write() function return the number of character it wrote
print(a)
f.close()

