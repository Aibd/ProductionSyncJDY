class Common:
    # 简道云参数
    api_key = "1ENC5lt8m3pf97kiKnATic26eTIXQKR5"
    app_id = "65bc6159daf9cea1dbb5be86"
    entry_id = "65e86b706509d73bea8b2d6e"

    # 简道云id查询数据包格式
    query_data = {
        "app_id": app_id,
        "entry_id": entry_id,
        "limit": 10000,
        "fields": ["_id", "billno"],
        "rel": "and",
        "filter": {
            "cond": [
                {
                    "field": "billno",
                    "method": "eq",
                    "value": 10
                },
                {
                    "field": "company",
                    "method": "eq",
                    "value": "希肤上海"
                }]
        }
    }
    # 简道云销售订单表单接口数据包格式
    jdy_production_data = {
        "op": "data_create",
        "app_id": app_id,
        "entry_id": entry_id,
        "transaction_id": "87cd7d71-c6df-4281-9927-469094395679",
        "data_list": [
            {
                "planorderno": {
                    "value": "Peter"
                },
                "billno": {
                    "value": "Peter"
                },
                "xfbillno": {
                    "value": "Peter"
                },
                "status": {
                    "value": "Peter"
                },
                "forder": {
                    "value": "Peter"
                },
                "cust": {
                    "value": "Peter"
                },
                "custno": {
                    "value": "Peter"
                },
                "custpno": {
                    "value": "Peter"
                },
                "estatus": {
                    "value": "Peter"
                },
                "pbtime": {
                    "value": "2018-01-01T10:10:10.000Z"
                },
                "pftime": {
                    "value": "2018-01-01T10:10:10.000Z"
                },
                "brandname": {
                    "value": "Peter"
                },
                "brandcode": {
                    "value": "Peter"
                },
                "prodcode": {
                    "value": "Peter"
                },
                "prodname": {
                    "value": "Peter"
                },
                "specmodel": {
                    "value": "Peter"
                },
                "batchno": {
                    "value": "Peter"
                },
                "unit": {
                    "value": "Peter"
                },
                "pqty": {
                    "value": 10
                },
                "diecutmethod": {
                    "value": "Peter"
                },
                "foldmethod": {
                    "value": "Peter"
                },
                "baggingmethod": {
                    "value": "Peter"
                },
                "irradiationmethod": {
                    "value": "Peter"
                },
                "packing": {
                    "value": "Peter"
                },
                "processclassification": {
                    "value": "Female"
                },
                "processname": {
                    "value": "Female"
                },
                "processcode": {
                    "value": "Peter"
                },
                "biller": {
                    "value": "jian"
                },
                "salesperson": {
                    "value": "jian"
                },
                "salesassistant": {
                    "value": "jian"
                },
                "msupervisor": {
                    "value": "jian"
                },
                "qsupervisor": {
                    "value": "jian"
                },
                "company": {
                    "value": "希肤"
                }
            }
        ],

    }
    #         "is_start_workflow": True

    # 简道云单条数据修改
    jdy_update_data = {
        "app_id": app_id,
        "entry_id": entry_id,
        "transaction_id": "87cd7d71-c6df-4281-9927-469094395677",
        "data_id": "",
        "data": {
            "planorderno": {
                "value": "Peter"
            },
            "billno": {
                "value": "Peter"
            },
            "xfbillno": {
                "value": "Peter"
            },
            "status": {
                "value": "Peter"
            },
            "forder": {
                "value": "Peter"
            },
            "cust": {
                "value": "Peter"
            },
            "custno": {
                "value": "Peter"
            },
            "custpno": {
                "value": "Peter"
            },
            "estatus": {
                "value": "Peter"
            },
            "pbtime": {
                "value": "2018-01-01T10:10:10.000Z"
            },
            "pftime": {
                "value": "2018-01-01T10:10:10.000Z"
            },
            "brandname": {
                "value": "Peter"
            },
            "brandcode": {
                "value": "Peter"
            },
            "prodcode": {
                "value": "Peter"
            },
            "prodname": {
                "value": "Peter"
            },
            "specmodel": {
                "value": "Peter"
            },
            "batchno": {
                "value": "Peter"
            },
            "unit": {
                "value": "Peter"
            },
            "pqty": {
                "value": 10
            },
            "diecutmethod": {
                "value": "Peter"
            },
            "foldmethod": {
                "value": "Peter"
            },
            "baggingmethod": {
                "value": "Peter"
            },
            "irradiationmethod": {
                "value": "Peter"
            },
            "packing": {
                "value": "Peter"
            },
            "processclassification": {
                "value": "Female"
            },
            "processname": {
                "value": "Female"
            },
            "processcode": {
                "value": "Peter"
            },
            "biller": {
                "value": "jian"
            },
            "salesperson": {
                "value": "jian"
            },
            "salesassistant": {
                "value": "jian"
            },
            "msupervisor": {
                "value": "jian"
            },
            "qsupervisor": {
                "value": "jian"
            },
            "company": {
                "value": "希肤"
            }
        }
    }
    # 查询的sql  广州
    ProductionGZ_query_sql = '''
        SELECT
               t3.FPlanOrderNo                                 生产计划编号,
               t1.FBillNo                                      生产任务单号,
               t1.FHeadSelfJ01107                              希肤任务单号,
               CASE
                   t1.FStatus
                   WHEN 0 THEN '计划'
                   WHEN 3 THEN '结案'
                   WHEN 5 THEN '确认'
                   ELSE '下达'
                   END                                         '单据状态',
               t2.FBillNo                                      销售订单,
               t5.FName                                        客户名称,
               t5.FNumber                                      客户编号,
               t1.FHeadSelfJ01109                              客户采购单号,
               t60.FMoStatusName                               执行状态,
               CONVERT(varchar, t1.FPlanCommitDate, 126) + 'Z' 计划开工日期,
               CONVERT(varchar, t1.FPlanFinishDate, 126) + 'Z' 计划完工日期,
               -- 产品明细
               t10.FAuxMasterName                              商品名,
               t10.FAuxMasterCode                              商品牌号,
               t10.FNumber                                     产品编码,
               t10.FName                                       产品名称,
               t10.FModel                                      '规格型号',
               t1.FGMPBatchNo                                  批号,
               t12.FName                                       '单位',
               CAST(t1.FQty AS FLOAT)                          计划生产数量,
               -- 加工要求
               t6.FName                                        冲切方式,
               t7.FName                                        折叠要求,
               t8.FName                                        入袋方式,
               t9.FName                                        辐照方式,
               t1.FHeadSelfJ0194                               包装要求,
               --工序
               t106.FName                                      工序分类,
               t107.FName                                      工序名称,
               t107.FID                                        工序编码,
               --用户
               t13.FName                                       制单人,
               t14.FName                                       销售代表,
               t15.FName                                       销售助理,
               t16.FName                                       生产主管,
               t17.FName                                       品质主管,
               '希肤广州'                                        公司
        FROM ICMO t1
                 LEFT JOIN SEOrder t2 ON t1.FOrderInterID = t2.FInterID
                 LEFT JOIN ICMrpResult t3 ON t1.FPlanOrderInterID = t3.FPlanOrderInterID
                 LEFT JOIN T_Emp t4 ON t1.FHeadSelfJ01103 = t4.FItemID
                 LEFT JOIN T_Organization t5 ON t1.FHeadSelfJ01106 = t5.FItemID
                 LEFT JOIN T_Item t6 ON t1.FHeadSelfJ0187 = t6.FItemID
                 LEFT JOIN T_Item t7 ON t1.FHeadSelfJ0189 = t7.FItemID
                 LEFT JOIN T_Item t8 ON t1.FHeadSelfJ0190 = t8.FItemID
                 LEFT JOIN T_Item t9 ON t1.FHeadSelfJ0192 = t9.FItemID
                 LEFT JOIN T_ICITEM t10 ON t1.FItemID = t10.FItemID
                 LEFT JOIN T_MeasureUnit t12 ON t10.FUnitID = t12.FMeasureUnitID
                 LEFT JOIN vw_ICMOStatus t60 ON t1.FInterID = t60.FInterID
                 LEFT JOIN t_SubMessage t106 ON t1.FHeadSelfJ01110 = t106.FInterID
                 LEFT JOIN t_SubMessage t107 ON t1.FHeadSelfJ01111 = t107.FInterID
                 LEFT JOIN T_User t13 ON t1.FBillerID = t13.FUserID
                 LEFT JOIN T_Emp t14 ON t1.FHeadSelfJ01100 = t14.FItemID
                 LEFT JOIN T_Emp t15 ON t1.FHeadSelfJ01105 = t15.FItemID
                 LEFT JOIN T_Emp t16 ON t1.FHeadSelfJ01101 = t16.FItemID
                 LEFT JOIN T_Emp t17 ON t1.FHeadSelfJ01104 = t17.FItemID
    '''
    # 插入本地Sqlite临时表temp
    insert_temp_sql = '''
        INSERT INTO temp (
            planorderno,
            billno,
            xfbillno,
            status,
            forder,
            cust,
            custno,
            custpno,
            estatus,
            pbtime,
            pftime,
            brandname,
            brandcode,
            prodcode,
            prodname,
            specmodel,
            batchno,
            unit,
            pqty,
            diecutmethod,
            foldmethod,
            baggingmethod,
            irradiationmethod,
            packing,
            processclassification,
            processname,
            processcode,
            biller,
            salesperson,
            salesassistant,
            msupervisor,
            qsupervisor,
            company
        ) VALUES (
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
            ?, ?, ?
        );
    '''
    # 插入本地Sqlite映射表
    insert_production_sql = '''
         INSERT INTO production (
            planorderno,
            billno,
            xfbillno,
            status,
            forder,
            cust,
            custno,
            custpno,
            estatus,
            pbtime,
            pftime,
            brandname,
            brandcode,
            prodcode,
            prodname,
            specmodel,
            batchno,
            unit,
            pqty,
            diecutmethod,
            foldmethod,
            baggingmethod,
            irradiationmethod,
            packing,
            processclassification,
            processname,
            processcode,
            biller,
            salesperson,
            salesassistant,
            msupervisor,
            qsupervisor,
            company
        ) VALUES (
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
            ?, ?, ?
        ); 
     '''

    # 简道云增量更新比对sql
    differences_sql = '''
        SELECT
            t1.planorderno,
            t1.billno,
            t1.xfbillno,
            t1.status,
            t1.forder,
            t1.cust,
            t1.custno,
            t1.custpno,
            t1.estatus,
            t1.pbtime,
            t1.pftime,
            t1.brandname,
            t1.brandcode,
            t1.prodcode,
            t1.prodname,
            t1.specmodel,
            t1.batchno,
            t1.unit,
            t1.pqty,
            t1.diecutmethod,
            t1.foldmethod,
            t1.baggingmethod,
            t1.irradiationmethod,
            t1.packing,
            t1.processclassification,
            t1.processname,
            t1.processcode,
            t1.biller,
            t1.salesperson,
            t1.salesassistant,
            t1.msupervisor,
            t1.qsupervisor,
            t1.company
        FROM temp t1
            LEFT JOIN production t2 ON COALESCE(t2.planorderno, 0) = COALESCE(t1.planorderno, 0)
                AND COALESCE(t2.custpno, 0) = COALESCE(t1.custpno, 0)
                AND t2.billno = t1.billno
                AND t2.xfbillno = t1.xfbillno
                AND t2.Status = t1.Status
                AND t2.pftime = t1.pftime
                AND t2.pbtime = t1.pbtime
                AND t2.pqty = t1.pqty
                AND t2.company = t1.company
        WHERE t1.company = '{company}' AND t2.billno is null 
    '''
    # 已删除数据比对sql
    deleted_query_sql = '''
        SELECT
            t1.planorderno,
            t1.billno,
            t1.xfbillno,
            t1.status,
            t1.forder,
            t1.cust,
            t1.custno,
            t1.custpno,
            t1.estatus,
            t1.pbtime,
            t1.pftime,
            t1.brandname,
            t1.brandcode,
            t1.prodcode,
            t1.prodname,
            t1.specmodel,
            t1.batchno,
            t1.unit,
            t1.pqty,
            t1.diecutmethod,
            t1.foldmethod,
            t1.baggingmethod,
            t1.irradiationmethod,
            t1.packing,
            t1.processclassification,
            t1.processname,
            t1.processcode,
            t1.biller,
            t1.salesperson,
            t1.salesassistant,
            t1.msupervisor,
            t1.qsupervisor,
            t1.company
        FROM production t1
            LEFT JOIN temp t2 ON t2.billno = t1.billno AND t2.company = t1.company
        WHERE t1.company = '{company}' AND t2.billno is null 
    '''
