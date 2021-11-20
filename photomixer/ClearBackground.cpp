#include "ClearBackground.h"

/*
This function will save the object image with transparent background
Input: image, black and white matte
Output: none
*/
void ClearBackground::getObjectImage(Mat image, Mat matte)
{
	//create new image
	Mat_<Vec4b> objectImage = Mat::zeros(image.size(), image.type());
	imwrite("objectImage.png", objectImage);

	//create alpha channel
	std::vector<Mat> matChannels;
	split(image, matChannels);
	Mat alpha = matChannels.at(BLUE) + matChannels.at(GREEN) + matChannels.at(RED);
	matChannels.push_back(alpha);
	merge(matChannels, objectImage);

	//change the backgroung alpha value to 0
	for (int i = 0; i < image.rows; i++)
	{
		for (int j = 0; j < image.cols; j++)
		{
			if (matte.at<Vec3b>(i, j)[RED] == BLACK) 
			{
				objectImage.at<Vec4b>(i, j)[ALPHA] = CLEAR;
			}
		}
	}

	//write changes to image
	imwrite("objectImage.png", objectImage);
}