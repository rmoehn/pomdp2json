/* A Bison parser, made by GNU Bison 3.0.4.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015 Free Software Foundation, Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

#ifndef YY_YY_HOME_ERLE_REPOS_PYTHON_RL_LIBPOMDP_SRC_PARSER_H_INCLUDED
# define YY_YY_HOME_ERLE_REPOS_PYTHON_RL_LIBPOMDP_SRC_PARSER_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token type.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    INTTOK = 1,
    FLOATTOK = 2,
    COLONTOK = 3,
    MINUSTOK = 4,
    PLUSTOK = 5,
    STRINGTOK = 6,
    ASTERICKTOK = 7,
    DISCOUNTTOK = 8,
    VALUESTOK = 9,
    STATETOK = 10,
    ACTIONTOK = 11,
    OBSTOK = 12,
    TTOK = 13,
    OTOK = 14,
    RTOK = 15,
    UNIFORMTOK = 16,
    IDENTITYTOK = 17,
    REWARDTOK = 18,
    COSTTOK = 19,
    RESETTOK = 20,
    STARTTOK = 21,
    INCLUDETOK = 22,
    EXCLUDETOK = 23,
    EOFTOK = 258
  };
#endif

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED

union YYSTYPE
{
#line 131 "/home/erle/repos/python-rl/libPOMDP/src/parser.y" /* yacc.c:1909  */

  Constant_Block *constBlk;
  int i_num;
  double f_num;

#line 87 "/home/erle/repos/python-rl/libPOMDP/src/parser.h" /* yacc.c:1909  */
};

typedef union YYSTYPE YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;

int yyparse (void);

#endif /* !YY_YY_HOME_ERLE_REPOS_PYTHON_RL_LIBPOMDP_SRC_PARSER_H_INCLUDED  */
