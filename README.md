# **Wireless-Joystick**
**Info:->**

This project is aimed at  providing a first hand tutorial to train images using dlib while creating a successful image processing project : wireless joystick. 

# **Algorithm**

**Step 1.** First task is to train a object as Joystick.

**Step 2.** Detect the object in the frame and decide it's position relative to the centre of camera.

**Step 3.** Assign integer values to the positions and send them from python script to Arduino using serial (UART) communication.

**Step 4.** Send the data from the base station Arduino to the controller Arduino of the bot through radio communication using NRF module.

**Step 5.** Control the bot direction of motion based on the data recieved from the NRF module.

# **WORKING**

### Step 1: Image Identification using deep learning library dlib.

Dlib is a modern C++ toolkit containing machine learning algorithms and tools for creating complex software in C++ to solve real world problems. 
It is used in both industry and academia in a wide range of domains including robotics, embedded devices, mobile phones, and large high performance computing environments. 
Let us see how we can use the power of dlib to train a python script to detect an object. 

Now the first and foremost thing that comes to our mind is...How should we make computer know about the type of object we want it to understand? To deal with
this problem dlib comes with a handy GUI tool called ImgLab. What ImgLab does is to create an .xml file of many pictures containing the object of interest while annotating images with object bounding
boxes.
`new word - annotating: simply means to mark`

First let's see how to do this and then we will understand how this .xml file is useful to the machine.

**How to use ImgLab**

Go to the ImgLab sub directory in your dlib directory. In my pc dlib is in home directory so "for me" the linux command will be:
`$ cd dlib/tools/imglab`

Then we will create a directory named 'build' which will do exactly as it sounds... build our cmake file for imglab tool, for it to be installed in our system. For linux, type this:
`$ mkdir build`
. Now we will go to this directory and make (or to say install) the file:
`cd build`

`cmake ..`

`cmake --build . --config Release`

Now hoping that everything goes right we must have imglab installed and ready to use. Now all we need is a lot of images to get started. Let's say our images are in folder: `/tmp/images`
then we can start imglab by:

`./imglab -c mydataset.xml /tmp/images` ..nothing happened? Well not entirely true! That particular command created an empty .xml file that will source it's images from the given directory.

    Is getting a large number of images a problem? No worries! I have attached a code to take multiple images, called getMultipleImages.py
    
Now that we have a lot of images and a tool ready...Let's start annotating!

First to open imglab GUI type this in your terminal:
`./imglab mydataset.xml`

Now once the window is open it is very important to understand the view...and possibly know all the shortcuts, because this annotating is a tiring task. 

Left panel which you can see loaded with words are the indexes or names of your images which are displayes at the center.
The central panel, written as Next Label, gives you the place to give your object a name (reference). Note that once you put a name in it, it stays for all the images... because that's what we are supposed to find, a single object in many images!

To select the object:

press and hold shift --> this creates a yellow coloured cross. This will give you an idea as to where the rectangle (that bounds it) will start.
left click, hold and drag --> till the rectangle becomes big enough to contain it.
Notice how the label is automaticaly placed.

Now suppose you made a mistake, then double click on the box and press delete.

Well suppose you made a smaller box than required.. no problem, hold shift and drag with right click!

After you have annotated all the images, go to file and choose save. Now you can safely exit the GUI. The generated .xml file is stored in the build directory.  
   
  