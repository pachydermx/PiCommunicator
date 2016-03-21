#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <wiringPi.h>
#include <unistd.h>
using namespace std;

//yama 0321 ->
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <stdlib.h>
#include <string.h>
//  <-

#define MOTOROUT1 14
#define MOTOROUT2 15
#define MOTORPWM 18
#define POW 1024

int main(void) {
	int i = 0;

	int flag = 0;

	int roll_f = 0;  //前進回数
	int roll_b = 0;  //後進回数

	//yama 0321 ->
	int sock;
	struct sockaddr_in addr;
	
	char buf[1024];

	sock = socket(AF_INET, SOCK_DGRAM, 0);

	addr.sin_family = AF_INET;
	addr.sin_port = htons(10001);
	addr.sin_addr.s_addr = INADDR_ANY;
//inet_addr("192.168.1.190");

	bind(sock, (struct sockaddr *)&addr, sizeof(addr));
	// <-
	
	if(wiringPiSetupGpio() == -1) {
		printf("setup error\n");
		return 1;
	}

	pinMode(MOTOROUT1, OUTPUT);  // GPIO14を出力に設定
	pinMode(MOTOROUT2, OUTPUT);
	pinMode(MOTORPWM, PWM_OUTPUT);

	digitalWrite(MOTOROUT1, 0);  // GPIO14に0Vを出力
	digitalWrite(MOTOROUT2, 0);
	digitalWrite(MOTORPWM, 0);

	while (1) {
		int temp_flag = flag;

		//cout << "input flag-->" ; cin >> flag;
		//getchar();

		//yama 0321 ->
		memset(buf, 0, sizeof(buf));
		recv(sock, buf, sizeof(buf), 0);

		flag = atoi(buf);
		// <-

		if(flag == 0) {			//前進
			if(temp_flag == 1){ //無駄
				pwmWrite(MOTORPWM, 0);
				digitalWrite(MOTOROUT2, 0);
				usleep(50000);
			}
			printf("forward\n");
			digitalWrite(MOTOROUT1, 1);
			pwmWrite(MOTORPWM, POW);
			usleep(10000);
			roll_f++;
			if(roll_f >= 5){
				roll_f = 0;
				pwmWrite(MOTORPWM, 0);
				digitalWrite(MOTOROUT1, 0);
				usleep(50000);
				flag = 1;
				roll_b = 1;
				printf("back\n");
				digitalWrite(MOTOROUT2, 1);
				pwmWrite(MOTORPWM, POW);
				usleep(100000);
			}
		}else if(flag == 1){	//後進
			if(temp_flag == 0){ //無駄
				pwmWrite(MOTORPWM, 0);
				digitalWrite(MOTOROUT1, 0);
				usleep(50000);
			}
			printf("back\n");
			digitalWrite(MOTOROUT2, 1);
			pwmWrite(MOTORPWM, POW);
			usleep(100000);
			roll_b++;
			if(roll_b >= 5){
				roll_b = 0;
				pwmWrite(MOTORPWM, 0);
				digitalWrite(MOTOROUT2, 0);
				usleep(50000);
				flag = 1;
				roll_f = 1;
				printf("forward\n");
				digitalWrite(MOTOROUT1, 1);
				pwmWrite(MOTORPWM, POW);
				usleep(100000);
			}
		}
			
		if(flag == 2) {	  //ストップ
			printf("stop\n");
			pwmWrite(MOTORPWM, 0);
			digitalWrite(MOTOROUT1, 0);
			digitalWrite(MOTOROUT2, 0);
			usleep(1000000);
			if(temp_flag == 0){
				flag = temp_flag;
				roll_f++;
				printf("forward\n");
				digitalWrite(MOTOROUT1, 1);
				pwmWrite(MOTORPWM, POW);
				usleep(100000);
			}else if(temp_flag == 1){
				flag = temp_flag;
				roll_b++;
				printf("back\n");
				digitalWrite(MOTOROUT2, 1);
				pwmWrite(MOTORPWM, POW);
				usleep(100000);	
			}

			

		}

	}

	return 0;

}