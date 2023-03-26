from Utilities.getframes import read_frames
from Utilities.getmetadata import get_meta_data
from Utilities.getpixelvalues import get_pixel_matrix
from Utilities.writeoutput import write_to_file
# save your video in TesData directory and then run the code.
vid_path = "TestData/demo.mp4"
img_path = "TestData/Frames/"

#main function
def ambient_matrix_info(vid_name):
    #show info about the video
    meta = get_meta_data(vid_path)
    print(meta)

    #clear the output
    file_to_delete = open("OutputCss/style.css",'w')
    file_to_delete.close()

    #write initial values to the output
    write_to_file(f'#video{{\n\tanimation: a1 {int(meta[0]/(meta[1]/2))}s linear forwards;\n}}\n')
    write_to_file(f'@keyframes a1{{\n\t')

    # import all the frames into the Frames directory
    read_frames(vid_path)

    # read the chroma subsampling values in a matrix
    for i in range(0,int(meta[0]),int(meta[1])):
        get_pixel_matrix(f'{img_path}Frame{i}',i,meta[0])
    
    # format the css
    with open('OutputCss/style.css', 'rb+') as fh:
        fh.seek(-1, 2)
        fh.truncate()
    write_to_file(f';}}\n')

#call to the main function
ambient_matrix_info(vid_path)