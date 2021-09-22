# nft_genertive_art
This python script is for creating generative art

Below is a list of dependencies to run this script

        Code Libraries/Packages
        
          python3 --> sudo apt-get update
        
                      sudo apt-get install python3.8
          
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
            
                layer0_variant1.png
                
                layer0_variant2.png
                
                ...
            
            trait2/
                
                layer1_variant1.png
                
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
        7) This does NOT generate the json metadata files, I'll be uploading a script to do that eventually (9/22/2021)      
