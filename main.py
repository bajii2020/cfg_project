# """
# imports
# """
from website import create_app


# """
# initialise
# """

app = create_app()


# """
# endpoints
# """


# """
# Run Flask
# # """

if __name__ == '__main__':
    app.run(debug=True)
