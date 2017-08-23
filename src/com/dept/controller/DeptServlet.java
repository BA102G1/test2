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

		    // 來自select_page.jsp的請求                                  // 來自 dept/listAllDept.jsp的請求
	
		
		if ("delete_Dept".equals(action)) { // 來自/dept/listAllDept.jsp的請求

			List<String> errorMsgs = new LinkedList<String>();
			req.setAttribute("errorMsgs", errorMsgs);
	
			try {
				/***************************1.接收請求參數***************************************/
				Integer deptno = new Integer(req.getParameter("deptno"));
				
				/***************************2.開始刪除資料***************************************/
				DeptService deptSvc = new DeptService();
				deptSvc.deleteDept(deptno);
				
				/***************************3.刪除完成,準備轉交(Send the Success view)***********/
				String url = "/dept/listAllDept.jsp";
				RequestDispatcher successView = req.getRequestDispatcher(url);// 刪除成功後, 成功轉交 回到 /dept/listAllDept.jsp
				successView.forward(req, res);
				
				/***************************其他可能的錯誤處理***********************************/
			} catch (Exception e) {
				errorMsgs.add("刪除資料失敗:"+e.getMessage());
				RequestDispatcher failureView = req
						.getRequestDispatcher("/dept/listAllDept.jsp");
				failureView.forward(req, res);
			}
		}

	}
}
