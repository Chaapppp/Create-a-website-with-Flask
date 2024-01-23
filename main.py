
# Import the create_app function from the 'website' module
from website import create_app

# Create an instance of the Flask application using the create_app function
app = create_app()

# Check if the script is being run directly (not imported as a module)
if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)
