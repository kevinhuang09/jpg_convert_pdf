from PIL import Image

# Convert a JPG image to PDF
def jpg_to_pdf(input_path, output_path):
    # Open the image
    image = Image.open(input_path)
    
    # Convert to RGB (important if the image has transparency)
    if image.mode in ("RGBA", "P"):
        image = image.convert("RGB")
    
    # Save as PDF
    image.save(output_path, "PDF", resolution=100.0)
    print(f"✅ Successfully converted '{input_path}' to '{output_path}'")

# Example usage
jpg_to_pdf("p001.jpg", "p001.pdf")
