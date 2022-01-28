﻿using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Text;
using System.Windows;
using System.Windows.Media;
using System.Windows.Media.Imaging;

namespace photomixerGUI
{
    public partial class Resize
    {
        private Communicator communicator = new Communicator();
        private static string objectPath;

        public Resize()
        {
            InitializeComponent();
        }

        // do a git pull origin develop in develop and in this brunch!!!!!
        public Resize(string ObjectImagePath)
        {
            InitializeComponent();

            // show the object image
            objectPath = Path.GetFullPath(ObjectImagePath);
            //ObjectImage.Source = new BitmapImage(new Uri(objectPath));

            // change here the size of the picture from the xaml according to my object picture ???
        }

        private void biggerButton_Click(object sender, RoutedEventArgs e)
        {
            bool flag = false;
            while (!flag)
            {
                bool fileExist = File.Exists(objectPath);
                if (fileExist)
                {
                    try
                    {
                        if (File.OpenRead(objectPath).CanRead)
                        {
                            flag = true;
                        }
                    }
                    catch (IOException)
                    {

                    }
                }
            }
            communicator.resizeObjectBigMsg(objectPath);
<<<<<<< HEAD

            //wait till the image is created to update the background image
            bool flag = false;
            while (!flag)
            {
                bool fileExist = File.Exists(objectPath);
                if (fileExist)
                {
                    try
                    {
                        if (File.OpenRead(objectPath).CanRead)
                        {
                            flag = true;
                        }
                    }
                    catch (IOException)
                    {

                    }
                }
            }

            ObjectImage.Source = new BitmapImage(new Uri(objectPath));
=======
            //ObjectImage.Source = new BitmapImage(new Uri(objectPath));
>>>>>>> 2cb9a75402af62083e5d68d931699e7d6cada17e
        }

        private void smallerButton_Click(object sender, RoutedEventArgs e)
        {
            communicator.resizeObjectSmallMsg(objectPath);
<<<<<<< HEAD

            //wait till the image is created to update the background image
            bool flag = false;
            while (!flag)
            {
                bool fileExist = File.Exists(objectPath);
                if (fileExist)
                {
                    try
                    {
                        if (File.OpenRead(objectPath).CanRead)
                        {
                            flag = true;
                        }
                    }
                    catch (IOException)
                    {

                    }
                }
            }

            ObjectImage.Source = new BitmapImage(new Uri(objectPath));
=======
            //ObjectImage.Source = new BitmapImage(new Uri(objectPath));
>>>>>>> 2cb9a75402af62083e5d68d931699e7d6cada17e
        }

        private void backButton_Click(object sender, RoutedEventArgs e)
        {
            //Edit editScreen = new Edit();
            //editScreen.Show();
            Close();
        }
    }
}
