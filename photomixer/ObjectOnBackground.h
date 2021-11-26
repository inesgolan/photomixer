#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <iostream>
#include <vector>

// BGR
#define BLUE 0
#define GREEN 1
#define RED 2
#define ALPHA 3

#define WHITE 255
#define BLACK 0

#define OPAQUE 255
#define CLEAR 0

using namespace cv;

class ObjectOnBackground
{
private: 
	Mat _background;
public:
	ObjectOnBackground(Mat); //c'tor
	~ObjectOnBackground(); //d'tor

	void setBackground(Mat); 
	Mat getBackground();

	Mat getEditedImage(int, int, Mat, Mat);
};

