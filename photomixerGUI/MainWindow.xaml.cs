﻿using System.Windows;
using System.IO;
using System.Windows.Media;
using System;

namespace photomixerGUI
{
    //this class is in charge of logining in the system
    public partial class MainWindow : Window
    {      
        public MainWindow()
        {
            InitializeComponent();
        }

        private void login(object sender, RoutedEventArgs e)
        {
            Communicator.loginMsg(Username.Text, Password.Password);

            File.OpenRead(ProjectVariables.OUTPUT_FILE_NAME);
            string text = File.ReadAllText(ProjectVariables.OUTPUT_FILE_NAME);

            if (text == "False")
            {
                ErrorMsg.Text = "Your own problem. go get new friends.";
                Username.Clear();
                Password.Clear();
            }
            else
            {
                ProjectVariables.username = Username.Text;
                
                Directory.CreateDirectory(ProjectVariables.username); //create folder for the username images

                //check if there are encrypted images
                //decrypt the user's images
                if (ProjectVariables.countOfEdits > 0)
                {
                    string[] images = Directory.GetFiles(ProjectVariables.username);
                    foreach (string image in images)
                    {
                        string[] splitPath = image.Split("\\");
                        string path = splitPath[splitPath.Length - 2] + "\\" + splitPath[splitPath.Length - 1];
                        Communicator.decryptionMsg(path, ProjectVariables.username);
                    }
                }

                Menu gotoMenu = new Menu();
                gotoMenu.Show();
                Close();
            }
        }

        // This function open the Register window
        private void register(object sender, RoutedEventArgs e)
        {
            Register goRegister = new Register();
            goRegister.Show();
            Close();
        }

        // This function enter to the app as a guest
        private void guestButton_click(object sender, RoutedEventArgs e)
        {
            ProjectVariables.username = "guest";
            Menu gotoMenu = new Menu();
            gotoMenu.Show();
            Close();
        }

        private void forgotPassword(object sender, RoutedEventArgs e)
        {
            Communicator.sendForgetPasswordMail(Username.Text);
        }
    }
}
