import sys
from app.openai_utils import OpenAIUtils
from app.project_generator import ProjectGenerator
from app.file_creator import FileCreator

def main():
    print("Welcome to the AI App Builder!")
    
    # Initialize OpenAIUtils
    openai_utils = OpenAIUtils()

    # Ask for app description
    app_description = input("Please enter a short description of your app: ")

    # Propose app name using OpenAI
    app_name = openai_utils.generate_app_name(app_description)
    app_name_confirmed = False
    while not app_name_confirmed:
        user_app_name = input(f"Proposed app name: {app_name}. Press Enter to confirm or type a new name: ")
        if user_app_name.strip() == "":
            app_name_confirmed = True
        else:
            app_name = user_app_name.strip()

    # Collect app features
    features = []
    while True:
        feature = input("Please enter a feature for your app (or type 'done' to finish): ")
        if feature.lower() == "done":
            break
        else:
            features.append(feature)

    # Generate project file structure using OpenAI
    project_structure = openai_utils.generate_project_structure(app_name, features)
    project_structure_confirmed = False
    while not project_structure_confirmed:
        user_feedback = input(f"Current project structure:\n{project_structure}\nType any comments or 'done' to confirm: ")
        if user_feedback.lower() == "done":
            project_structure_confirmed = True
        else:
            project_structure = openai_utils.update_project_structure(user_feedback, project_structure)

    # Create files and folders structure in Workspace directory
    project_generator = ProjectGenerator(app_name)
    project_generator.create_project_structure(project_structure)

    # Create content for each individual file using OpenAI
    file_creator = FileCreator(project_generator.workspace_directory, openai_utils)
    file_creator.create_project_files(project_structure)

    print("Project successfully created!")

if __name__ == "__main__":
    main()
