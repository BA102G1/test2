<%@ page contentType="text/html; charset=UTF-8" pageEncoding="Big5"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ page import="java.util.*"%>
<%@ page import="com.emp.model.*"%>
<%-- 絤策蹦ノ EL 糶猭 --%>

<%  
// EmpService empSvc = new EmpService();
// List<EmpVO> list = empSvc.getAll();
// pageContext.setAttribute("list",list);
%>
<jsp:useBean id="deptSvc" scope="page" class="com.dept.model.DeptService" />

<html>
<head>
<title>┮Τ场 - listAllDept.jsp</title>
</head>
<body bgcolor='white'>
<b><font color=red>絤策蹦ノ EL 糶猭:</font></b>
<table border='1' cellpadding='5' cellspacing='0' width='800'>
	<tr bgcolor='orange' align='center' valign='middle' height='20'>
		<td>
		<h3>┮Τ场 - ListAllDept.jsp</h3>
		<a href="<%=request.getContextPath()%>/select_page.jsp"><img src="images/back1.gif" width="100" height="32" border="0"></a>
		</td>
	</tr>
</table>

<%-- 岿粇 --%>
<c:if test="${not empty errorMsgs}">
  <font color='red'>叫タ岿粇:
  <ul>
  <c:forEach var="message" items="${errorMsgs}">
    <li>${message}</li>
  </c:forEach>
  </ul>
  </font>
</c:if>

<table border='1' bordercolor='#CCCCFF' width='800'>
	<tr>
		<th>场絪腹</th>
		<th>场嘿</th>
		<th>场膀</th>
		<th>э</th>
		<th>埃<font color=red>(闽羛代刚籔ユ-み)</font></th>
		<th>琩高场</th>
	</tr>
	
	<c:forEach var="deptVO" items="${deptSvc.all}">
		<tr align='center' valign='middle'>
			<td>${deptVO.deptno}</td>
			<td>${deptVO.dname}</td>
			<td>${deptVO.loc}</td>
			<td>
			  <FORM METHOD="post" ACTION="<%=request.getContextPath()%>/dept/dept.do">
			    <input type="submit" value="э" disabled="true"> 
			    <input type="hidden" name="deptno" value="${deptVO.deptno}">
			    <input type="hidden" name="action" value="getOne_For_Update_Dept">
			</td></FORM>
			<td>
			  <FORM METHOD="post" ACTION="<%=request.getContextPath()%>/dept/dept.do">
			    <input type="submit" value="埃">
			    <input type="hidden" name="deptno" value="${deptVO.deptno}">
			    <input type="hidden" name="action" value="delete_Dept">
			</td></FORM>
			<td>
			  <FORM METHOD="post" ACTION="<%=request.getContextPath()%>/dept/dept.do">
			    <input type="submit" value="癳琩高"> 
			    <input type="hidden" name="deptno" value="${deptVO.deptno}">
			    <input type="hidden" name="action" value="listEmps_ByDeptno_B">
			</td></FORM>
		</tr>
	</c:forEach>
</table>

<%if (request.getAttribute("listEmps_ByDeptno")!=null){%>
       <jsp:include page="listEmps_ByDeptno.jsp" />
<%} %>

</body>
</html>
