package com.dept.controller;

import java.io.*;
import java.util.*;

import javax.servlet.*;
import javax.servlet.http.*;

import com.dept.model.*;
import com.emp.model.*;

public class DeptServlet extends HttpServlet {

	public void doGet(HttpServletRequest req, HttpServletResponse res)
			throws ServletException, IOException {
		doPost(req, res);
	}

	public void doPost(HttpServletRequest req, HttpServletResponse res)
			throws ServletException, IOException {

		req.setCharacterEncoding("UTF-8");

		String action = req.getParameter("action");

		    // �Ӧ�select_page.jsp���ШD                                  // �Ӧ� dept/listAllDept.jsp���ШD
	
		
		if ("delete_Dept".equals(action)) { // �Ӧ�/dept/listAllDept.jsp���ШD

			List<String> errorMsgs = new LinkedList<String>();
			req.setAttribute("errorMsgs", errorMsgs);
	
			try {
				/***************************1.�����ШD�Ѽ�***************************************/
				Integer deptno = new Integer(req.getParameter("deptno"));
				
				/***************************2.�}�l�R�����***************************************/
				DeptService deptSvc = new DeptService();
				deptSvc.deleteDept(deptno);
				
				/***************************3.�R������,�ǳ����(Send the Success view)***********/
				String url = "/dept/listAllDept.jsp";
				RequestDispatcher successView = req.getRequestDispatcher(url);// �R�����\��, ���\��� �^�� /dept/listAllDept.jsp
				successView.forward(req, res);
				
				/***************************��L�i�઺���~�B�z***********************************/
			} catch (Exception e) {
				errorMsgs.add("�R����ƥ���:"+e.getMessage());
				RequestDispatcher failureView = req
						.getRequestDispatcher("/dept/listAllDept.jsp");
				failureView.forward(req, res);
			}
		}

	}
}
