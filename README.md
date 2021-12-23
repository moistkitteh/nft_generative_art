# nft_genertive_art
This python script is for creating generative art.

The files and subfolders within this repository are all set up to be able to run this out of the box with the example setup. If you run this script from the command line with the following,

        python3 generative_art.py

this should run without issue to generate 36 images in the images/ folder based on the traits in the traits/ folder and the weights in weights.dat. It will also update the
rarity.csv and imagetraits.csv files, which are tables which respectively describe the rarity of different traits and the traits associated with each image

Below are all of the necessary dependencies, files/directories to make, and variables to set before you run the code

        Code Libraries/Packages
          python3 --> sudo apt-get update
                      sudo apt-get install python3.8
          Numpy   --> python3 -m pip install --upgrade numpy
          PIL     --> python3 -m pip install --upgrade Pillow          
          random  --> (installed with python3)
        
        Files (These need to be made before running)           
           weights.dat -- list of all of the desired weights for each trait           
           tnames.dat -- list of the actual trait names
           
        Directories (These directories need to be built ahead of time)
           images/ -- directory to store generated images [name changeable]
           traits/ -- directory that trait images will be pulled up from. Layers will be added alphabetically/numerical by directory name
          
        User Set Variables (These are set within the code)
           nf -- final number of art pieces you want
           dout -- directory to store all of the created image
           dtraits -- directory where all traits are stored

To make the metadata json files, first you need to create an account on an IPFS system like Pinata, and upload the directory (not the individual files) containing all of your generated images. Once you've done that, write down the CID of the directory you uploaded. Each of the images are saved as https://gateway.pinata.cloud/ipfs/CID/image0.png, where the CID is the address of the directory and the image0.png is the filename of the image you uploaded that is within that directory. This allows us to easily loop through all of the images you uploaded. Once you have the CID written down, make the following directory in your project folder and set the following variables in the file make_metadata.py
       
      Directories
        metadata/ = directory that the metadata files will be saved to
       
      User Set Variables
        iname = default filename you used for the images you generated (in the example, the images are image0.py, image1.py)
        itype = the file extension you exported the generated images as (ex, .png)
        address = the web address plus the CID you stored the directory at (ex, "https://gateway.pinata.cloud/ipfs/CID", where CID is the directory CID you wrote down)
        mpath = local path to the folder you want all of the metadata files saved at
        descr = description you want saved in all of your metadata files

Once those variables are set, run the make_metadata.py file with the following

        python3 make_metadata.py

Directory Structure:

     nft_art_main/
        generative_art.py
        tnames.dat
        weights.dat
        images/
                image0.png
                image1.png
                ...
        traits/
            trait1/
                layer1_variant1.png       
                layer1_variant2.png     
                ...  
            trait2/    
                layer2_variant1.png     
                layer2_variant2.png
                ...
            trait3/ 
             

   Notes:
   
        1) The subdirectories in traits/ will be parsed alphanumerically, meaning that the first directory name that is encountered 
               will be the bottom layer/background, the second dirctory name will be the layer above the background, etc. The filenames
               within the subdirectories will also be parsed alphanumerically and assigned weights that way as well. For example,
               in the weights.dat file the very first weight will be linked to the first alphanumeric file within the first alphanumeric
               trait directory. In the provided example, trait1/Green.png is linked with the weight of 0.60 in the weights.dat file, and trait1/Pink.png
               is linked with the weight of 0.30 in the weights.dat file, etc.   
        2) All of the weights MUST add up to a sum total of 1.0, the code will likely break if they do not.         
        3) There MUST be the same number of names in tnames.dat as there are subdirectories within traits/        
        4) There MUST be the same number of weights as there are total image files within all of the traits/ subdirectories        
        5) jpg files don't allow you to make anything transparent, and while jpg is usable within the code it's a better practice to use .png files        
        6) The code will output a rarity table and a masterlist that links each image # to all of the traits it posseses. These are .csv's and can be viewed in excel or 
               an equivalent program
