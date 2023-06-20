from datetime import datetime
import os

from PIL import Image, ImageDraw, ImageFont
import requests

def write_content(certificate_path: str, default_font_path: str, 
                  content_font_path: str, logo_url: str, org_bio:str):
    
    logo_pos = (100, 150)
    bio_pos = (320, 270)
    
    date_pos = (120, 450)
    name_pos = (120, 550)
    issue_pos = (120,750)
    pr_pos = (355, 820)
    
    logo_img = Image.open(requests.get(logo_url, stream=True).raw).convert("RGBA")
       
    # opens the image
    img = Image.open(certificate_path, mode ='r')
    
    # overlays image
    img.paste(logo_img, logo_pos, mask = logo_img)
    
        # gets the image width
    image_width = img.width
          
        # gets the image height
    image_height = img.height 
   
        # creates a drawing canvas overlay 
        # on top of the image
    draw = ImageDraw.Draw(img)
   
    # gets the font object from the 
    # font file (TTF)
    
    name_font = ImageFont.truetype(
            content_font_path,
            70 # change this according to your needs
        )
    org_name_font = ImageFont.truetype(
            content_font_path,
            40 # change this according to your needs
        )
    
    default_font = ImageFont.truetype(
            default_font_path,
            24 # change this according to your needs
        )
    
    date_font = ImageFont.truetype(
            content_font_path,
            28 # change this according to your needs
        )
    
    issue_font = ImageFont.truetype(
            content_font_path,
            32 # change this according to your needs
        )
    
    pr_font = ImageFont.truetype(
            content_font_path,
            30 # change this according to your needs
        )
    
    # Writing the content on the image 
    draw.text((320,200), org_name,
            fill="black", font = org_name_font)
    
    draw.text(bio_pos, org_bio,
            fill="black", font = default_font)
    
    draw.text(date_pos, date_of_contribution,
            fill="black", font = date_font)
    
    draw.text(name_pos,contributor_name,
            fill="black", font = name_font)
    
    draw.text((120,690),"has successfully solved the issue",
            fill="black", font = default_font)
    
    draw.text(issue_pos, issue_name,
            fill="black", font = issue_font)
    
    draw.text((120, 820), "with the Pull Request",
            fill="black", font = default_font)
    
    draw.text(pr_pos, pr_name, fill="grey", font = pr_font)
    
    draw.text((120, 860), "on the Github Repository",
            fill="black", font = default_font)
    
    draw.text((395, 860), repo_url,
            fill="grey", font = default_font)
    
    draw.text((120, 1050), "Verify at:", fill="black",
             font=default_font)
    
    draw.text((220,1050), repo_url+ '/issues/' + issue_id, font= default_font,fill="black")
    
    # save image with contributor name in the working path
    img.save(f"{contributor_name}.png")

    

# {
# Driver Code starts
if __name__ == "__main__":
    # Grab variable values based on env varaibles inside.yml
    org_profile_url = os.environ["org_profile_url"]
    repo_name = os.environ["repo_name"]
    date = os.environ["date"]
    contributor_name = os.environ["contributor_name"]
    issue_name = os.environ["issue_title"]
    pr_name = os.environ["pr_name"]
    logo_url = os.environ["logo_url"] + "&s=200"
    org_bio = os.environ["org_bio"]
    issue_id = os.environ["issue_number"]
    
    date_of_contribution = str(datetime.fromisoformat(date[:-1] + '+00:00').date())
    
    

    repo_url = org_profile_url + f'/{repo_name}'
    org_name = org_profile_url[19:].capitalize()

    
    print("Excecuting generate_certificate.py ")
    
    # These are accessed later by few functions
    template_path = "certificate-template.png"
    # this will access fonts from Pillow folders
    default_font_path = "Pillow/Certificate-template-fonts/Roboto-Regular.ttf"
    content_font_path = "Pillow/Certificate-template-fonts/AnonymousPro-Regular.ttf"

    
    ## Function calls
    write_content(template_path, default_font_path, content_font_path, logo_url,
             org_bio)
    
    print(f"Created Certificate with name {contributor_name}.png")

# } Driver Code ends
